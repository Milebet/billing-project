from django.db import models
#from django.contrib.contenttypes.fields import GenericForeignKey
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes.fields import GenericRelation
#
#class Bank(models.Model):
#	name = models.CharField(max_length=300, unique=True)
#	description = models.TextField()
#
#class Payment(models.Model):
#	date = models.DateTimeField()
#	amount = models.DecimalField( max_digits=20, decimal_places=10)
#	observations = models.TextField()
#	OPTIONS_PAYMENT = (('counted','De contado'),('credit','A crédito'))
#	payment_mode = models.CharField(max_length=10, choices=OPTIONS_PAYMENT, default='counted',)
#	request_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default="")
#	request_id = models.PositiveIntegerField(default=0)
#	request = GenericForeignKey('request_type','request_id')
#
#class PaymentMethod(models.Model):
#	OPTIONS_PAYMENT = (('cash','Efectivo'),('card','Tarjeta'),('check','Cheque'))
#	payment_method = models.CharField(max_length=10, choices=OPTIONS_PAYMENT, default='cash',)
#	request_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default="")
#	request_id = models.PositiveIntegerField(default=0)
#	detail = GenericForeignKey('request_type','request_id')
#	payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
#
#class Card(models.Model):
#	number_card = models.IntegerField()
#	expired_date = models.DateTimeField()
#	owner_name = models.CharField(max_length=300)
#	bank = models.ForeignKey(Bank, on_delete=models.CASCADE, default="")
#	payment_method = GenericRelation(PaymentMethod)
#
#class Check(models.Model):
#	number_ref = models.IntegerField()
#	turn_date = models.DateTimeField()
#	payment_date = models.DateTimeField()
#	owner_name = models.CharField(max_length=300)
#	amount = models.DecimalField( max_digits=20, decimal_places=10)
#	OPTIONS_STATUS = (('pending','En Proceso'),('charged','Cobrado'),('canceled', 'Anulado'),('rejected','Rebotado'),('expired','Vencido'),('invalid','Invalido'))
#	status = models.CharField(max_length=10, choices=OPTIONS_STATUS, default='pending',)
#	bank = models.ForeignKey(Bank, on_delete=models.CASCADE, default="")
#	payment_method = GenericRelation(PaymentMethod)
