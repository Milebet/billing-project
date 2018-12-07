from django.contrib.auth.models import AbstractUser
from django.db import models
from people.models import Person
from billingstore.models import Brand
#from django.contrib.auth.decorators import login_required

#https://www.youtube.com/watch?v=5x97gGspzjY
#https://docs.djangoproject.com/en/2.1/topics/auth/customizing/

#@login_required(login_url='login/')

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

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'