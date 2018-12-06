from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages 
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser
from .forms import CustomUserCreationForm, UserCreationMultiForm, CustomUserChangeForm, CustomChangePasswordForm
from people.models import Person
from billingstore.models import Company, Brand
from people.forms import EditProfileForm

#Home users
def Home(request):
	company = Company.objects.first()
	return render(request,'registration/home.html',{'company': company})

#index users
def Index(request):
	users = CustomUser.objects.all()
	return render(request,'users/index.html',{'users': users})

#Register users
def sign_up(request):
	if request.method == 'POST':
		form = UserCreationMultiForm(data=request.POST)
		if form.is_valid():
			person = Person()
			person.document_type = form['person']['document_type'].data
			person.document_id = form['person']['document_id'].data
			person.first_name = form['person']['first_name'].data
			person.second_name = form['person']['second_name'].data
			person.last_name = form['person']['last_name'].data
			person.second_last_name = form['person']['second_last_name'].data
			person.direction = form['person']['direction'].data
			person.save()
			user = form['user'].save(commit=False)
			user.person = person
			user.save()
			messages.success(request,('The user has been created..'))
			return redirect('index')
		else:
			messages.error(request,"The form has errors")
			form = UserCreationMultiForm(data=request.POST)
	else:
		form = UserCreationMultiForm()
	
	context = {'form': form}
	return render(request, 'registration/signup.html',context)

#log out session
def logout_user(request):
	logout(request)
	messages.success(request,('Yu have been logged out'))
	return redirect('home')

#change password
def change_password(request, user_id):
	user = CustomUser.objects.get(id=user_id)
	if request.method == 'POST':
		form = CustomChangePasswordForm(data=request.POST, user= user )
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request,('You have updated your password...'))
			return redirect('users:personal_info', user)
		else:
			messages.error(request,('Something went wrong'))
			form = CustomChangePasswordForm(data=request.POST, user= user)
	else:
		form = CustomChangePasswordForm(user= user)
	
	context = {'form': form, 'user_id': user.id}
	return render(request, 'users/change_password.html',context)

def edit_user(request, user_id):
	user = CustomUser.objects.get(id = user_id)
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance= user )
		if form.is_valid():
			form.save()
			messages.success(request,('You have Edited your User Account...'))
			return redirect('users:personal_info',user_id)
		else:
			messages.error(request,('Something went wrong'))
			form = CustomUserChangeForm(request.POST, instance= user)
	else:
		form = CustomUserChangeForm(instance= user)
	
	context = {'form': form, 'user_id': user_id}
	return render(request, 'users/edit_account.html',context)

def show_user(request,user_id):
	user = get_object_or_404(CustomUser,id=user_id)
	return render(request,'people/my_profile.html',{'user':user})

#view for personal info (name, last nae)
def personal_info(request, user_id):
	user = CustomUser.objects.get(id=user_id)
	return render(request,'people/my_profile.html',{'user': request.user})

#view for update personal info (name, last name)
def update_info_person(request, user_id):
	user = CustomUser.objects.get(id=user_id)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= user.person )
		if form.is_valid():
			form.save()
			messages.success(request,('You have Edited your Profile...'))
			return redirect('users:personal_info', user.id)
		else:
			messages.error(request,('Something went wrong'))
			form = EditProfileForm(request.POST, instance= user.person)
	else:
		form = EditProfileForm(instance= user.person)
	
	context = {'form': form, 'user_id': user_id}
	return render(request, 'people/edit_info.html',context)