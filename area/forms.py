from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import SelectMultiple
from .models import AreaModel

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = '__all__'
        labels = {
            'area' : 'Area'
        }
        widgets = {
            'area' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            )
        }
