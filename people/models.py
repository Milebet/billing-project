from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify
from django.utils import timezone

#crear los documents primero por shell
class DocumentType(models.Model):
	OPTIONS_DOCS = (('cedula','Cédula de Identidad'),('passport', 'Pasaporte'),('ruc','RUC/RISE'))
	name = models.CharField(max_length=10, choices=OPTIONS_DOCS, default='cedula',)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-name']
		verbose_name = 'DocumentType'
		verbose_name_plural = 'DocumentTypes'

class PersonType(models.Model):
	OPTIONS_PERSON = (('natural','Natural'),('juridical', 'Juridico'))
	name = models.CharField(max_length=10, choices=OPTIONS_PERSON, default='natural',)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-name']
		verbose_name = 'PersonType'
		verbose_name_plural = 'PeopleType'

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
	document_id = models.CharField(max_length=10, unique=True)
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)
	second_last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=100)
	direction = models.TextField()
	document_type = models.ForeignKey(DocumentType, on_delete=models.SET_DEFAULT, default='', null=True)
	person_type = models.ForeignKey(PersonType, on_delete=models.SET_DEFAULT, default=1, null=True)
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

#class RolPersona(models.Model):
#	person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE)
#	person = models.ForeignKey(Person, on_delete=models.CASCADE)
