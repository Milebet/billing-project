from django import forms
from django.forms import ModelForm
from .models import Division, Line, Category

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

		self.fields['description'].widget.attrs['class'] = 'form-control'
		self.fields['description'].widget.attrs['placeholder'] = 'Inrese un breve texto'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].label = 'Estatus'

		self.fields['company'].widget.attrs['class'] = 'form-control'
		self.fields['company'].label = 'Compañia'

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

		self.fields['description'].widget.attrs['class'] = 'form-control'
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

	def __init__(self, *args, **kwargs):
		super(LineForm,self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['name'].label = 'Nombre Linea'
		self.fields['name'].help_text = '<span class="form-text text-muted"><small>Ejemplo: Carne roja, carne blanca</small></span>'

		self.fields['description'].widget.attrs['class'] = 'form-control'
		self.fields['description'].widget.attrs['placeholder'] = 'Inrese un breve texto'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].label = 'Estatus'

		self.fields['line'].widget.attrs['class'] = 'form-control'
		self.fields['line'].label = 'Line'

		self.fields['parent'].widget.attrs['class'] = 'form-control'
		self.fields['parent'].label = 'Categoria padre'