from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm
from .models import Division, Line, Category #, Unit, Equivalence, Product, InactiveProduct
from django.contrib import admin

class DivisionForm(ModelForm):
	
	class Meta:
		model = Division
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(DivisionForm,self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['name'].label = 'Nombre División'
		self.fields['name'].help_text = '<span class="form-text text-muted"><small>Ejemplo: Carne, Embutidos, etc</small></span>'

		self.fields['description'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['description'].widget.attrs['placeholder'] = 'Inrese un breve texto'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].label = 'Estatus'

		self.fields['company'].widget.attrs['class'] = 'form-control'
		self.fields['company'].label = 'Compañia'
		self.fields['company'].widget.attrs['disabled'] = True
		self.fields['company'].required = False

class LineForm(ModelForm):
	
	class Meta:
		model = Line
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(LineForm,self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['name'].label = 'Nombre Linea'
		self.fields['name'].help_text = '<span class="form-text text-muted"><small>Ejemplo: Carne roja, carne blanca</small></span>'

		self.fields['description'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['description'].widget.attrs['placeholder'] = 'Inrese un breve texto'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].label = 'Estatus'

		self.fields['division'].widget.attrs['class'] = 'form-control'
		self.fields['division'].label = 'Divición'

class CategoryForm(ModelForm):
	
	class Meta:
		model = Category
		fields = '__all__'
		fields_order = ('line', 'parent', 'name', 'description', 'status')

	def __init__(self, *args, **kwargs):
		super(CategoryForm,self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['name'].label = 'Nombre Cateoria'
		self.fields['name'].help_text = '<span class="form-text text-muted"><small>Ejemplo:</small></span>'

		self.fields['description'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['description'].widget.attrs['placeholder'] = 'Ingrese un breve texto'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].label = 'Estatus'

		self.fields['line'].widget.attrs['class'] = 'form-control'
		self.fields['line'].label = 'Line'

		self.fields['parent'].widget.attrs['class'] = 'form-control'
		self.fields['parent'].label = 'Categoria padre'
		self.fields['parent'].required = False 

#class UnitForm(ModelForm):
#	
#	class Meta:
#		model = Unit
#		fields = '__all__'
#
#	def __init__(self, *args, **kwargs):
#		super(UnitForm,self).__init__(*args, **kwargs)
#
#		self.fields['name'].widget.attrs['class'] = 'form-control'
#		self.fields['name'].label = 'Unidad de Medida'
#
#class EquivalenceForm(ModelForm):
#	
#	class Meta:
#		model = Equivalence
#		fields = '__all__'
#
#	def __init__(self, *args, **kwargs):
#		super(EquivalenceForm,self).__init__(*args, **kwargs)
#
#		self.fields['base_unit'].widget.attrs['class'] = 'form-control'
#		self.fields['base_unit'].label = 'Unidad de Medida'
#		self.fields['equivalence_unit'].widget.attrs['class'] = 'form-control'
#		self.fields['equivalence_unit'].label = 'Unidad de Equivalencia'
#		self.fields['value'].widget.attrs['class'] = 'form-control'
#		self.fields['value'].label = 'Valor'
#
#class ProductForm(ModelForm):
#	
#	class Meta:
#		model = Product
#		fields = '__all__'
#		fields_order = ('category', 'unit', 'code','full_name', 'short_name', 'description', 'stock', 'sale_price', 'base_unit', 'status')

#
#	def __init__(self, *args, **kwargs):
#		super(ProductForm,self).__init__(*args, **kwargs)
#
#		self.fields['code'].widget.attrs['class'] = 'form-control'
#		self.fields['code'].widget.attrs['placeholder'] = 'Introduzca un valor'
#		self.fields['code'].label = 'Código Producto'
#
#		self.fields['full_name'].widget.attrs['class'] = 'form-control'
#		self.fields['full_name'].widget.attrs['placeholder'] = 'Introduzca un valor'
#		self.fields['full_name'].label = 'Nombre Completo'
#
#		self.fields['short_name'].widget.attrs['class'] = 'form-control'
#		self.fields['short_name'].widget.attrs['placeholder'] = 'Introduzca un valor'
#		self.fields['short_name'].label = 'Nombre Corto'
#		self.fields['short_name'].help_text = '<span class="form-text text-muted"><small>Ejemplo: Carne, Embutidos, etc</small></span>'
#
#		self.fields['description'].widget =  admin.widgets.AdminTextareaWidget()
#		self.fields['description'].label = 'Descripción'
#
#		self.fields['stock'].widget.attrs['class'] = 'form-control'
#		self.fields['stock'].widget.attrs['placeholder'] = 'Introduzca un valor'
#		self.fields['stock'].label = 'Stock'
#
#		self.fields['sale_price'].widget.attrs['class'] = 'form-control'
#		self.fields['sale_price'].widget.attrs['placeholder'] = 'Introduzca un valor'
#		self.fields['sale_price'].label = 'Precio de Venta'
#
#		self.fields['base_unit'].widget.attrs['class'] = 'form-control'
#		self.fields['base_unit'].label = 'Unidad Base'
#
#		self.fields['status'].widget.attrs['class'] = 'form-control'
#		self.fields['status'].label = 'Estatus'
#
#		self.fields['category'].widget.attrs['class'] = 'form-control'
#		self.fields['category'].label = 'Categoria'
#
#		self.fields['unit'].widget.attrs['class'] = 'form-control'
#		self.fields['unit'].label = 'Unidad'
#
#class InactiveProductForm(ModelForm):
#	
#	class Meta:
#		model = InactiveProduct
#		fields = '__all__'
#
#	def __init__(self, *args, **kwargs):
#		super(InactiveProductForm,self).__init__(*args, **kwargs)
#
#		self.fields['register_at'].widget.attrs['class'] = 'form-control'
#		self.fields['register_at'].label = 'Registrado el:'
#
#		self.fields['quantity'].widget.attrs['class'] = 'form-control'
#		self.fields['quantity'].widget.attrs['placeholder'] = 'Introduzca un valor'
#		self.fields['quantity'].label = 'Cantidad'
#
#		self.fields['reason'].widget.attrs['class'] = 'form-control'
#		self.fields['reason'].label = 'Motivo de Baja'
#
#		self.fields['product'].widget.attrs['class'] = 'form-control'
#		self.fields['product'].label = 'Producto'
