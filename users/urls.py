from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
app_name = "users"

urlpatterns = [
	#path('signup/', views.SignUp.as_view(), name='signup'),
	path('signup/', views.sign_up, name='signup'),
	path('edit/<int:user_id>', views.edit_user, name='edit'),
	path('logout/', views.logout_user, name='logout'),
	path('index/', views.Index, name='index'),
	path('password_reset/',PasswordResetView.as_view(), name='reset_password'),
	path('reset-password/done/', PasswordChangeDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('change_password/<int:user_id>',views.change_password, name='change_password'),
	path('<int:user_id>/',views.show_user, name='show_user'),
	path('edit_personal_info/<int:user_id>',views.update_info_person, name="update_info_person"),
	path('personal_info/<int:user_id>',views.personal_info, name='personal_info'),
]