from django.shortcuts import render, redirect
from .forms import DivisionForm
from .models import Division

def index_division(request):
	return render(request,'products/divisions.html')

def RegisterProduct(request):
	return render(request,'products/register.html')

def IndexProducts(request):
	return render(request,'products/index.html')

def CurrentStock(request):
	return render(request,'products/stock.html')

def DamagedProducts(request):
	return render(request,'products/damaged.html')

def add_division(request):
	if request.method == 'POST':
		form = DivisionForm(request.POST, instance= request.division )
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new division...'))
			return redirect('home')
	else:
		form = DivisionForm(instance= request.division)
	
	context = {'form': form}
	return render(request, 'products/add_division.html',context)