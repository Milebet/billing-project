from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class Phone(models.Model):
	request_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default="")
	request_id = models.PositiveIntegerField(default=0)
	request = GenericForeignKey('request_type','request_id')
	phone_number = models.IntegerField()
	OPTIONS_PHONE = (('cellphone','Célular'),('local', 'Local'),)
	phone_type = models.CharField(max_length=10, choices=OPTIONS_PHONE, default='cellphone',)

	def __str__(self):
		return self.phone_number

	class Meta:
		verbose_name = 'phone'
		verbose_name_plural = 'phones'

class Person(models.Model):
	OPTIONS_DOCS = (('cedula','Cédula de Identidad'),('passport', 'Pasaporte'),('ruc','RUC/RISE'))
	document_type = models.CharField(max_length=10, choices=OPTIONS_DOCS, default='cedula',)
	document_id = models.CharField(max_length=10, unique=True)
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)
	second_last_name = models.CharField(max_length=30, blank=True)
	direction = models.TextField()
	phones = GenericRelation(Phone)
	register_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.first_name + " " + self.last_name

	def register_date_pretty(self):
		return self.register_at.strftime('%b %e %Y')

	class Meta:
		get_latest_by = 'register_at'
		ordering = ['-register_at']
		verbose_name = 'person'
		verbose_name_plural = 'people'
