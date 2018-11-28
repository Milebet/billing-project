from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from django.utils import timezone
from people.models import Phone
from .validators import validate_ruc

class Company(models.Model):
	phones = GenericRelation(Phone)
	document_id = models.CharField(max_length=13, unique=True, validators=[validate_ruc])
	name = models.CharField(max_length=100)
	direction = models.TextField()
	description = models.TextField(blank=True)
	OPTIONS_STATUS = (('active','Active'),('inactive', 'Inactive'),)
	status = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='active',)
	register_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

	def register_date_pretty(self):
		return self.register_at.strftime('%b %e %Y')

	class Meta:
		get_latest_by = 'register_at'
		ordering = ['-register_at']
		verbose_name = 'company'
		verbose_name_plural = 'companies'

class City(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'city'
		verbose_name_plural = 'cities'

class Brand(models.Model):
	name = models.CharField(max_length=100)
	direction = models.TextField()
	description = models.TextField(blank=True)
	OPTIONS_STATUS = (('active','Active'),('inactive', 'Inactive'),)
	status = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='active',)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
	cities = models.ManyToManyField(City)
	phones = GenericRelation(Phone)
	register_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

	def register_date_pretty(self):
		return self.register_at.strftime('%b %e %Y')

	class Meta:
		get_latest_by = 'register_at'
		ordering = ['-register_at']
		verbose_name = 'brans'
		verbose_name_plural = 'brands'
