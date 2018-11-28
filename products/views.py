from django.shortcuts import render, redirect
from .forms import DivisionForm, LineForm , CategoryForm, UnitForm, EquivalenceForm, ProductForm
from .models import Division, Line, Category, Unit, Equivalence, Product
from django.contrib import messages 

def RegisterProduct(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new product...'))
			return redirect('home')
	else:
		form = ProductForm()
	
	context = {'form': form}
	return render(request, 'products/register.html',context)

def IndexProducts(request):
	products = Product.objects.all()
	return render(request,'products/index.html',{'products':products})

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

def index_category(request):
	categories = Category.objects.all()
	return render(request,'products/categories.html',{'categories': categories})

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new category...'))
			return redirect('home')
	else:
		form = CategoryForm()
	
	context = {'form': form}
	return render(request, 'products/add_category.html',context)

def index_unit(request):
	units = Unit.objects.all()
	return render(request,'products/units.html',{'units': units})

def add_unit(request):
	if request.method == 'POST':
		form = UnitForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new unit...'))
			return redirect('home')
	else:
		form = UnitForm()
	
	context = {'form': form}
	return render(request, 'products/add_unit.html',context)

def index_equivalence(request):
	equivalences = Equivalence.objects.all()
	return render(request,'products/equivalences.html',{'equivalences': equivalences})

def add_equivalence(request):
	if request.method == 'POST':
		form = EquivalenceForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new equivalence...'))
			return redirect('home')
	else:
		form = EquivalenceForm()
	
	context = {'form': form}
	return render(request, 'products/add_equivalent.html',context)