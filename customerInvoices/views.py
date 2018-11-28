from django.shortcuts import render

def RegisterCustomer(request):
	return render(request,'customerInvoices/register.html')

def IndexCustomers(request):
	return render(request,'customerInvoices/index.html')

def GenareteInvoice(request):
	return render(request,'customerInvoices/generate_invoice.html')

def SearchInvoice(request):
	return render(request,'customerInvoices/search_invoice.html')