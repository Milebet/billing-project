from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['username', 'password', 'email', 'last_login','date_joined', 'status_user']
	fieldsets = (
		(None, {'fields': ('username', 'password', 'email')}),
		('Admin info', {'fields': ('status_user','rol_user')}),
		)
	add_fieldsets = (
    	(None, {
    		'classes': ('wide',),
    		'fields': ('status_user', 'rol_user',)}
    		),
    	)

admin.site.register(CustomUser, CustomUserAdmin)
