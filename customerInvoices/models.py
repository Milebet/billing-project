from django.db import models
#from people.models import Person
#from billingstore.models import Company, Brand
#from products.models import Product
#from users.models import CustomUser
#from payments.models import Payment
#from django.contrib.contenttypes.fields import GenericRelation
#
#class Customer(models.Model):
#	last_purchase_date = models.DateTimeField()
#	person = models.OneToOneField(
#        Person,
#        on_delete=models.CASCADE,
#        primary_key=True,
#    )
#
#class InvoiceSale(models.Model):
#	register_at = models.DateTimeField()
#	discount = models.DecimalField( max_digits=20, decimal_places=10)
#	vat = models.DecimalField( max_digits=20, decimal_places=10)
#	subtotal = models.DecimalField( max_digits=20, decimal_places=10)
#	total = models.DecimalField( max_digits=20, decimal_places=10)
#	observation = models.TextField()
#	first_name = models.CharField(max_length=100)
#	second_name = models.CharField(max_length=100)
#	last_name = models.CharField(max_length=100)
#	second_last_name = models.CharField(max_length=100)
#	address = models.TextField()
#	phone_number = models.IntegerField()
#	OPTIONS_STATUS = (('approved','Aprovada'),('canceled', 'Anulado'))
#	status = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='approved',)
#	brand = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT, default='')
#	client = models.ForeignKey(Customer, on_delete=models.SET_DEFAULT, default='')
#	user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default='')
#	payments = GenericRelation(Payment)
#
#class InvoiceSaleDetail(models.Model):
#	quantity = models.IntegerField()
#	base_unit = models.CharField(max_length=50,default="")
#	unit_pvp = models.DecimalField( max_digits=20, decimal_places=10)
#	subtotal = models.DecimalField( max_digits=20, decimal_places=10)
#	discount = models.DecimalField( max_digits=20, decimal_places=10)
#	total = models.DecimalField( max_digits=20, decimal_places=10)
#	invoice = models.ForeignKey(InvoiceSale, on_delete=models.SET_DEFAULT, default='')
#	product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='')
#
#class CustomerCompany(models.Model):
#	company = models.ForeignKey(Company, on_delete=models.CASCADE)#
#	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)