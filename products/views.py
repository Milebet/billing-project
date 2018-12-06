from django.shortcuts import render, redirect, get_object_or_404
from .forms import DivisionForm, LineForm, CategoryForm #, UnitForm, EquivalenceForm, ProductForm, InactiveProductForm
from .models import Division, Line, Category #, Unit, Equivalence, Product, InactiveProduct
from django.contrib import messages 

def index_division(request):
	divisions = Division.objects.all()
	return render(request,'products/division/divisions.html',{'divisions': divisions})

def add_division(request):
	if request.method == 'POST':
		form = DivisionForm(request.POST)
		#form['division']['company'] = "Carniceria"
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new division...'))
			return redirect('products:index_division')
		else:
			messages.error(request,('Your form has some errors...'))
			form = DivisionForm()
	else:
		form = DivisionForm()
	
	context = {'form': form}
	return render(request, 'products/division/add_division.html',context)

def edit_division(request, division_id):
	division = Division.objects.get(id=division_id)
	if request.method == 'POST':
		form = DivisionForm(request.POST, instance=division)
		if form.is_valid():
			form.save()
			messages.success(request,('Los datos de la empresa han sido actualizados...'))
			return redirect('products:show_division', division.id)
		else:
			messages.error(request,('Something went wrong'))
			form = DivisionForm(request.POST, instance=division)
	else:
		form = DivisionForm(instance=division)
	
	context = {'form': form, 'division_id': division_id}
	return render(request, 'products/division/edit_division.html',context)

def show_division(request,division_id):
	division = get_object_or_404(Division,id=division_id)
	return render(request,'products/division/show_division.html',{'division': division})

def index_lines(request):
	lines = Line.objects.all()
	return render(request,'products/line/lines.html',{'lines': lines})

def add_lines(request):
	if request.method == 'POST':
		form = LineForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new line...'))
			return redirect('products:index_lines')
		else:
			messages.error(request,('Your form has some errors...'))
			form = LineForm()
	else:
		form = LineForm()
	
	context = {'form': form}
	return render(request, 'products/line/add_lines.html',context)

def edit_line(request, line_id):
	line = Line.objects.get(id=line_id)
	if request.method == 'POST':
		form = LineForm(request.POST, instance=line)
		if form.is_valid():
			form.save()
			messages.success(request,('Los datos de la linea han sido actualizados...'))
			return redirect('products:show_line', line.id)
		else:
			messages.error(request,('Something went wrong'))
			form = LineForm(request.POST, instance=line)
	else:
		form = LineForm(instance=line)
	
	context = {'form': form, 'line_id': line_id}
	return render(request, 'products/line/edit_line.html',context)

def show_line(request,line_id):
	line = get_object_or_404(Line,id=line_id)
	return render(request,'products/line/show_line.html',{'line': line})

def index_category(request):
	categories = Category.objects.all()
	return render(request,'products/category/categories.html',{'categories': categories})

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('You have added a new category...'))
			return redirect('products:index_category')
		else:
			messages.error(request,('Your form has some errors...'))
			form = CategoryForm()
	else:
		form = CategoryForm()
	
	context = {'form': form}
	return render(request, 'products/category/add_category.html',context)

def edit_category(request, category_id):
	category = Category.objects.get(id=category_id)
	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			form.save()
			messages.success(request,('Los datos de la Categoria han sido actualizados...'))
			return redirect('products:show_category', category.id)
		else:
			messages.error(request,('Something went wrong'))
			form = CategoryForm(request.POST, instance=category)
	else:
		form = CategoryForm(instance=category)
	
	context = {'form': form, 'category_id':category_id}
	return render(request, 'products/category/edit_category.html',context)

def show_category(request,category_id):
	category = get_object_or_404(Category,id=category_id)
	return render(request,'products/category/show_category.html',{'category': category})

#def RegisterProduct(request):
#	if request.method == 'POST':
#		form = ProductForm(request.POST)
#		if form.is_valid():
#			form.save()
#			messages.success(request,('You have added a new product...'))
#			return redirect('home')
#	else:
#		form = ProductForm()
#	
#	context = {'form': form}
#	return render(request, 'products/register.html',context)
#
#def IndexProducts(request):
#	products = Product.objects.all()
#	return render(request,'products/index.html',{'products':products})
#
#def CurrentStock(request):
#	return render(request,'products/stock.html')
#
#def DamagedProducts(request):
#	return render(request,'products/damaged.html')
#
#def index_unit(request):
#	units = Unit.objects.all()
#	return render(request,'products/units.html',{'units': units})
#
#def add_unit(request):
#	if request.method == 'POST':
#		form = UnitForm(request.POST)
#		if form.is_valid():
#			form.save()
#			messages.success(request,('You have added a new unit...'))
#			return redirect('home')
#	else:
#		form = UnitForm()
#	
#	context = {'form': form}
#	return render(request, 'products/add_unit.html',context)
#
#def index_equivalence(request):
#	equivalences = Equivalence.objects.all()
#	return render(request,'products/equivalences.html',{'equivalences': equivalences})
#
#def add_equivalence(request):
#	if request.method == 'POST':
#		form = EquivalenceForm(request.POST)
#		if form.is_valid():
#			form.save()
#			messages.success(request,('You have added a new equivalence...'))
#			return redirect('home')
#	else:
#		form = EquivalenceForm()
#	
#	context = {'form': form}
#	return render(request, 'products/add_equivalent.html',context)
#
#def DamagedProducts(request):
#	inactives = InactiveProduct.objects.all()
#	return render(request,'products/damaged.html',{'inactive_products': inactives})
#
#def add_inactiveproduct(request):
#	if request.method == 'POST':
#		form = InactiveProductForm(request.POST)
#		if form.is_valid():
#			form.save()
#			messages.success(request,('You have inactive a product...'))
#			return redirect('home')
#	else:
#		form = InactiveProductForm()
#	
#	context = {'form': form}#
#	return render(request, 'products/add_inactiveproduct.html',context)