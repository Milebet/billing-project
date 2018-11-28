from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from people.models import Person
from people.forms import PersonForm
from betterforms.multiform import MultiModelForm

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username','status_user', 'rol_user')

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Introduzca su nombre de usuario.'
		self.fields['username'].label = 'Nombre de Usuario'
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Letras de la a-z, digitos son aceptados.</small></span>'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Introduzca su contraseña.'
		self.fields['password1'].label = 'Contraseña'
		self.fields['password1'].help_text = '<span class="form-text text-muted"><small><ul><li>La contraseña no debe ser similar a cualquiera de su información personal.</li><li>Debe contener al menos 8 caracteres.</li><li>No use una contraseña facil o común.</li><li>La contraseña debe poseer letras y digitos.</li></ul></small></span>'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Repita la contraseña.'
		self.fields['password2'].label = 'Confirmar Contraseña'
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small> Introduzca la misma contraseña. Para verificación.</small></span>'
		self.fields['status_user'].widget.attrs['class'] = 'form-control'
		self.fields['status_user'].label = 'Estatus'
		self.fields['status_user'].help_text = '<span class="form-text text-muted"><small> Seleccione alguna de las dos opciones.</small></span>'
		self.fields['rol_user'].widget.attrs['class'] = 'form-control'
		self.fields['rol_user'].label = 'Tipo de Usuario'
		self.fields['rol_user'].help_text = '<span class="form-text text-muted"><small> Seleccione alguna de las dos opciones.</small></span>'

class UserCreationMultiForm(MultiModelForm):
	form_classes = {
		'person': PersonForm,
		'user': CustomUserCreationForm
	}
	field_order = ['user','person']

class CustomUserChangeForm(UserChangeForm):
	password = forms.CharField(label="", max_length=100, widget= forms.TextInput(attrs={'type':'hidden'}))

	class Meta(UserChangeForm):
		model = CustomUser
		fields = ('username','status_user', 'rol_user', 'password')

	def __init__(self, *args, **kwargs):
		super(CustomUserChangeForm,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].label = 'Nombre de Usuario'
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Letras de la a-z, digitos son aceptados.</small></span>'
		self.fields['status_user'].widget.attrs['class'] = 'form-control'
		self.fields['status_user'].label = 'Estatus'
		self.fields['status_user'].help_text = '<span class="form-text text-muted"><small> Seleccione alguna de las dos opciones.</small></span>'
		self.fields['rol_user'].widget.attrs['class'] = 'form-control'
		self.fields['rol_user'].label = 'Tipo de Usuario'
		self.fields['rol_user'].help_text = '<span class="form-text text-muted"><small> Seleccione alguna de las dos opciones.</small></span>'
		