from django.db import models
#from django.contrib.contenttypes.fields import GenericRelation
#from people.models import Phone
#from billingstore.models import Company, Brand
#from products.models import Product
#from users.models import CustomUser
#from payments.models import Payment

#class Provider(models.Model):
#	phones = GenericRelation(Phone)
#	document_id = models.IntegerField(unique=True)
#	name = models.CharField(max_length=200)
#	direction = models.TextField()
#	OPTIONS_STATUS = (('active','Active'),('inactive', 'Inactive'),)
#	status = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='active',)

#class InvoicePusrchase(models.Model):
#	register_at = models.DateTimeField()
#	name = models.CharField(max_length=200)
#	address = models.TextField()
#	phone_number = models.IntegerField()
#	subtotal = models.DecimalField( max_digits=20, decimal_places=10)
#	discount = models.DecimalField( max_digits=20, decimal_places=10)
#	vat = models.DecimalField( max_digits=20, decimal_places=10)
#	total = models.DecimalField( max_digits=20, decimal_places=10)
#	OPTIONS_STATUS = (('approved','Aprovada'),('canceled', 'Anulado'))
#	status = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='approved',)
#	brand = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default='')
#	provider = models.ForeignKey(Provider, on_delete=models.SET_DEFAULT, default='')
#	user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default='')
#	payments = GenericRelation(Payment)

#class InvoicePurchaseDetail(models.Model):
#	quantity = models.IntegerField()
#	base_unit = models.CharField(max_length=50, default="")
#	unit_cost = models.DecimalField( max_digits=20, decimal_places=10)
#	subtotal = models.DecimalField( max_digits=20, decimal_places=10)
#	discount = models.DecimalField( max_digits=20, decimal_places=10)
#	total = models.DecimalField( max_digits=20, decimal_places=10)
#	invoice = models.ForeignKey(InvoicePusrchase, on_delete=models.CASCADE, default='')
#	product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='')

#class ProviderCompany(models.Model):
#	company = models.ForeignKey(Company, on_delete=models.CASCADE)
#	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

