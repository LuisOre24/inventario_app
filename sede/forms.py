from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import SelectMultiple
from .models import SedeModel

class SedeForm(forms.ModelForm):
    class Meta:
        model = SedeModel
        fields = '__all__'
        labels = {
            'sede' : 'Sede'
        }
        widgets = {
            'sede' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese la Sede'
                }
            ),
            'direccion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese la Direccion'
                }
            )
        }
