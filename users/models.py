from django.contrib.auth.models import AbstractUser
from django.db import models
from people.models import Person
from billingstore.models import Brand
#from django.contrib.auth.decorators import login_required

#@login_required(login_url='login/')

class CustomUser(AbstractUser):
	id = models.AutoField(auto_created=True, primary_key=True, serialize=False, default=1)
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