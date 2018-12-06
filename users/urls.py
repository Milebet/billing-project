from django.urls import path
from . import views
app_name = "users"

urlpatterns = [
	#path('signup/', views.SignUp.as_view(), name='signup'),
	path('signup/', views.sign_up, name='signup'),
	path('edit/<int:user_id>', views.edit_user, name='edit'),
	path('logout/', views.logout_user, name='logout'),
	path('index/', views.Index, name='index'),
	path('change_password/<int:user_id>',views.change_password, name='change_password'),
	path('<int:user_id>/',views.show_user, name='show_user'),
	path('edit_personal_info/<int:user_id>',views.update_info_person, name="update_info_person"),
	path('personal_info/<int:user_id>',views.personal_info, name='personal_info'),
]