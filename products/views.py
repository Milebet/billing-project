from django.shortcuts import render, redirect
from .forms import DivisionForm, LineForm
from .models import Division, Line
from django.contrib import messages 

def RegisterProduct(request):
	return render(request,'products/register.html')

def IndexProducts(request):
	return render(request,'products/index.html')

def CurrentStock(request):
	return render(request,'products/stock.html')

def DamagedProducts(request):
	return render(request,'products/damaged.html')

def index_division(request):
	divisions = Division.objects.all()
	return render(request,'products/divisions.html',{'divisions': divisions})

def add_division(request):
	if request.method == 'POST':
		form = DivisionForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new division...'))
			return redirect('home')
	else:
		form = DivisionForm()
	
	context = {'form': form}
	return render(request, 'products/add_division.html',context)

def index_lines(request):
	lines = Line.objects.all()
	return render(request,'products/lines.html',{'lines': lines})

def add_lines(request):
	if request.method == 'POST':
		form = LineForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new lines...'))
			return redirect('home')
	else:
		form = LineForm()
	
	context = {'form': form}
	return render(request, 'products/add_lines.html',context)