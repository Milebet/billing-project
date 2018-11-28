from django.shortcuts import render,redirect
from .forms import EditProfileForm
from django.contrib import messages 

def update_info_person(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= request.user.person )
		if form.is_valid():
			form.save()
			messages.success(request,('You have Edited your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance= request.user.person)
	
	context = {'form': form}
	return render(request, 'people/edit_info.html',context)

def my_personal_info(request):
	return render(request,'people/my_profile.html',{'user': request.user})
