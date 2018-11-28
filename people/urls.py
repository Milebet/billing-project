from django.urls import path
from . import views 

urlpatterns = [
	path('edit_info/',views.update_info_person, name="update_info_person"),
	path('my_personal_info/',views.my_personal_info, name='my_personal_info'),
]