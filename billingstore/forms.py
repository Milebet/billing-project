from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm
from .models import Company, Brand
from django.contrib import admin

class CompanyForm(ModelForm):

	class Meta:
		model = Company
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CompanyForm,self).__init__(*args, **kwargs)

		self.fields['document_id'].widget.attrs['class'] = 'form-control'
		self.fields['document_id'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['document_id'].label = 'Número de Documento'
		self.fields['document_id'].help_text = '<span class="form-text text-muted"><small>Introduzca el número de Ruc </small></span>'

		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['name'].label = 'Nombre'

		self.fields['direction'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['direction'].widget.attrs['placeholder'] = 'Indique la dirección'
		self.fields['direction'].label = 'Dirección'

		self.fields['description'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['description'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['status'].label = 'Estatus'
		self.fields['status'].widget.attrs['disabled'] = True
		self.fields['status'].required = False

		self.fields['register_at'].widget.attrs['class'] = 'form-control'
		self.fields['register_at'].label = 'Registrado el:'
		self.fields['register_at'].dissabled = True
		self.fields['register_at'].required = False
		self.fields['register_at'].widget.attrs['disabled'] = True
		self.fields['register_at'].required = False

class BrandForm(ModelForm):

	class Meta:
		model = Brand
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(BrandForm,self).__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['name'].label = 'Nombre'

		self.fields['direction'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['direction'].widget.attrs['placeholder'] = 'Indique la dirección'
		self.fields['direction'].label = 'Dirección'

		self.fields['description'].widget =  admin.widgets.AdminTextareaWidget()
		self.fields['description'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['description'].label = 'Descripción'

		self.fields['status'].widget.attrs['class'] = 'form-control'
		self.fields['status'].widget.attrs['placeholder'] = 'Introduzca un valor'
		self.fields['status'].label = 'Estatus'
		self.fields['status'].widget.attrs['disabled'] = True
		self.fields['status'].required = False

		self.fields['company'].widget.attrs['class'] = 'form-control'
		self.fields['company'].label = 'Compañia'
		self.fields['company'].widget.attrs['disabled'] = True
		self.fields['company'].required = False

		self.fields['register_at'].widget.attrs['class'] = 'form-control'
		self.fields['register_at'].label = 'Registrado el:'
		self.fields['register_at'].dissabled = True
		self.fields['register_at'].required = False
		self.fields['register_at'].widget.attrs['disabled'] = True
		self.fields['register_at'].required = False