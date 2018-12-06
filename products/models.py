from django.db import models
from billingstore.models import Company, Brand

class Division(models.Model):
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField()
	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
	company = models.ForeignKey(Company, on_delete=models.SET_DEFAULT, default=1)

	def __str__(self):
		return self.name

class Line(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
	division = models.ForeignKey(Division, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
	line = models.ForeignKey(Line, on_delete=models.CASCADE, default=1)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name

#class Unit(models.Model):
#	OPTIONS = (('kg','Kilogramo'),('lb','Libra'))
#	name = models.CharField(max_length=100, choices=OPTIONS, default='kg')
#
#	def __str__(self):
#		return self.name
#
#class Equivalence(models.Model):
#	OPTIONS = (('kg','Kilogramo'),('lb','Libra'))
#	base_unit = models.CharField(max_length=50, choices=OPTIONS, default='kg')
#	equivalence_unit = models.CharField(max_length=50, choices=OPTIONS, default='kg')
#	value = models.DecimalField( max_digits=20, decimal_places=10)
#	unit = models.ManyToManyField(Unit)
#
#	def __str__(self):
#		return self.base_unit
#
#class Product(models.Model):
#	code = models.CharField(max_length=100, unique=True)
#	full_name = models.CharField(max_length=200)
#	short_name = models.CharField(max_length=200)
#	description = models.TextField()
#	stock = models.IntegerField()
#	sale_price = models.DecimalField( max_digits=20, decimal_places=10)
#	OPTIONS = (('kg','Kilogramo'),('lb','Libra'))
#	base_unit = models.CharField(max_length=50, choices=OPTIONS, default='kg')
#	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
#	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
#	category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
#	unit = models.ForeignKey(Unit, on_delete=models.SET_DEFAULT, default=1)
#
#	def __str__(self):
#		return self.full_name
##
##
#class AlternateCode(models.Model):
#	code = models.CharField(max_length=100, unique=True)
#	description = models.TextField()
#	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
#	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
#	product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
#
#	def __str__(self):
#		return self.code
##
#class InactiveProduct(models.Model):
#	register_at = models.DateTimeField()
#	quantity = models.IntegerField()
#	reason = models.TextField()
#	product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=1)
#
#	def __str__(self):
#		return self.id
##
#class ProductBrand(models.Model):
#	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
#	product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
#	quantity = models.IntegerField()
#	pvp_brand = models.DecimalField( max_digits=20, decimal_places=10)
#	pvp = models.DecimalField( max_digits=20, decimal_places=10)
#	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
#	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
#
#	def __str__(self):
#		return self.id

#
#
