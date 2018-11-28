from django import forms
from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
	
	class Meta:
		model = Person
		fields = '__all__'
		exclude = ("register_at",)

	field_order = ['person_type','document_type','document_id','first_name','second_name','last_name','second_last_name','direction','email']

	def __init__(self, *args, **kwargs):
		super(PersonForm,self).__init__(*args, **kwargs)

		self.fields['document_type'].widget.attrs['class'] = 'form-control'
		self.fields['document_type'].label = 'Tipo de Documento'

		self.fields['person_type'].widget.attrs['class'] = 'form-control'
		self.fields['person_type'].label = 'Tipo de Persona'

		self.fields['document_id'].widget.attrs['class'] = 'form-control'
		self.fields['document_id'].widget.attrs['placeholder'] = 'Introduzca su documento de identidad'
		self.fields['document_id'].label = 'Número de Documento'
		self.fields['document_id'].help_text = '<span class="form-text text-muted"><small>Formato valido de acuerdo al tipo de documento seleccionado</small></span>'

		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre 1'
		self.fields['first_name'].label = 'Primer Nombre'

		self.fields['second_name'].widget.attrs['class'] = 'form-control'
		self.fields['second_name'].widget.attrs['placeholder'] = 'Nombre 2'
		self.fields['second_name'].label = 'Segundo Nombre'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido 1'
		self.fields['last_name'].label = 'Primer Apellido'

		self.fields['second_last_name'].widget.attrs['class'] = 'form-control'
		self.fields['second_last_name'].widget.attrs['placeholder'] = 'Apellido 2'
		self.fields['second_last_name'].label = 'Segundo Apellido'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Introduzca su correo electrónico'
		self.fields['email'].label = 'Correo Electrónico'
		self.fields['email'].help_text = '<span class="form-text text-muted"><small>nombre@dominio.com</small></span>'

		self.fields['direction'].widget.attrs['class'] = 'form-control'
		self.fields['direction'].label = 'Dirección'

class EditProfileForm(ModelForm):
	class Meta:
		model = Person
		fields = ('first_name','second_name','last_name','second_last_name','email','direction')

	def __init__(self, *args, **kwargs):
		super(EditProfileForm,self).__init__(*args, **kwargs)

		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre 1'
		self.fields['first_name'].label = 'Primer Nombre'

		self.fields['second_name'].widget.attrs['class'] = 'form-control'
		self.fields['second_name'].widget.attrs['placeholder'] = 'Nombre 2'
		self.fields['second_name'].label = 'Segundo Nombre'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido 1'
		self.fields['last_name'].label = 'Primer Apellido'

		self.fields['second_last_name'].widget.attrs['class'] = 'form-control'
		self.fields['second_last_name'].widget.attrs['placeholder'] = 'Apellido 2'
		self.fields['second_last_name'].label = 'Segundo Apellido'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Introduzca su correo electrónico'
		self.fields['email'].label = 'Correo Electrónico'
		self.fields['email'].help_text = '<span class="form-text text-muted"><small>nombre@dominio.com</small></span>'

		self.fields['direction'].widget.attrs['class'] = 'form-control'
		self.fields['direction'].label = 'Dirección'
