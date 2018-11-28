from django.db import models
from billingstore.models import Company, Brand

class Division(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
	company = models.ForeignKey(Company, on_delete=models.SET_DEFAULT, default=1)

class Line(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
	division = models.ForeignKey(Division, on_delete=models.CASCADE, default=1)

#class Unit(models.Model):
#	name = models.CharField(max_length=100)
#
class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
	line = models.ForeignKey(Line, on_delete=models.CASCADE, default=1)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)

#class Product(models.Model):
#	code = models.CharField(max_length=100, unique=True)
#	full_name = models.CharField(max_length=200)
#	short_name = models.CharField(max_length=200)
#	description = models.TextField()
#	stock = models.IntegerField()
#	sale_price = models.DecimalField( max_digits=20, decimal_places=10)
#	base_unit = models.CharField(max_length=50)
#	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
#	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
#	category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='')
#	unit = models.ForeignKey(Unit, on_delete=models.SET_DEFAULT, default='')
#
#class Equivalence(models.Model):
#	base_unit = models.CharField(max_length=50)
#	equivalence_unit = models.CharField(max_length=50)
#	value = models.DecimalField( max_digits=20, decimal_places=10)
#	unit = models.ManyToManyField(Unit)
#
#class AlternateCode(models.Model):
#	code = models.CharField(max_length=100, unique=True)
#	description = models.TextField()
#	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
#	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)
#	product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
#
#class InactiveProduct(models.Model):
#	register_at = models.DateTimeField()
#	quantity = models.IntegerField()
#	reason = models.TextField()
#	product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='')
#
#class ProductBrand(models.Model):
#	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#	product = models.ForeignKey(Product, on_delete=models.CASCADE)
#	quantity = models.IntegerField()
#	pvp_brand = models.DecimalField( max_digits=20, decimal_places=10)
#	pvp = models.DecimalField( max_digits=20, decimal_places=10)
#	OPTION_STATUS = (('active','Activo'),('inactive','Inactivo'))
#	status = models.CharField(max_length=10, choices=OPTION_STATUS, default='active',)



