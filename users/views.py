from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, UserCreationMultiForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from people.models import Person, DocumentType
from billingstore.models import Company, Brand
from .models import CustomUser
from django.contrib import messages 

class SignUp(generic.CreateView):
	form_class = UserCreationMultiForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

	def form_valid(self,form):
		person = Person()
		person.document_id = form['person']['document_id'].data
		person.first_name = form['person']['first_name'].data
		person.second_name = form['person']['second_name'].data
		person.last_name = form['person']['last_name'].data
		person.second_last_name = form['person']['second_last_name'].data
		person.email = form['person']['email'].data
		person.direction = form['person']['direction'].data
		person.document_type = DocumentType.objects.first()
		person.save()
		user = form['user'].save(commit=False)
		user.person = person
		user.save()
		return redirect('home')

def logout_user(request):
	logout(request)
	messages.success(request,('Yu have been logged out'))
	return redirect('home')

def Home(request):
	company = Company.objects.first()
	return render(request,'registration/home.html',{'company': company})

def Index(request):
	return render(request,'users/index.html')

def edit_user(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance= request.user )
		if form.is_valid():
			form.save()
			messages.success(request,('You have Edited your User Account...'))
			return redirect('home')
	else:
		form = CustomUserChangeForm(instance= request.user)
	
	context = {'form': form}
	return render(request, 'users/edit_account.html',context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user= request.user )
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request,('You have changed your password...'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user= request.user)
	
	context = {'form': form}
	return render(request, 'users/change_password.html',context)