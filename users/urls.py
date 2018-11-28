from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('edit/', views.edit_user, name='edit'),
	path('logout/', views.logout_user, name='logout'),
	path('index/', views.Index, name='index'),
	path('change_password/',views.change_password, name='change_password')
]