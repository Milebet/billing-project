from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from people.models import Person
from billingstore.models import Brand
from django.utils import timezone
from django.core.mail import send_mail
#from django.contrib.auth.decorators import login_required

#https://www.youtube.com/watch?v=5x97gGspzjY
#https://docs.djangoproject.com/en/2.1/topics/auth/customizing/

#@login_required(login_url='login/')
class CustomUserManager(BaseUserManager):
	def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()

		user = self.model(username = username,
						is_staff= is_staff, is_active= True,
						is_superuser= is_superuser, last_login=now,
						date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self,username, password=None, **extra_fields):
		return self._create_user(username, password, False, False, **extra_fields)

	def create_superuser(self, username, password, **extra_fields):
		return self._create_user(username, password, True, True, **extra_fields)

class CustomUser(AbstractUser):
	OPTIONS_STATUS = (('active','Activo'),('inactive', 'Inactivo'),)
	status_user = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='active',)
	OPTIONS_ROL = (('admin','Administrador'),('seller', 'Vendedor'),)
	rol_user = models.CharField(max_length=10, choices=OPTIONS_ROL, default='admin',)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1,)
	person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        default=1
    )

	objects = CustomUserManager()

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.username)

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email,[self.email])
