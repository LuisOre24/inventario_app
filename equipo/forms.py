from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import SelectMultiple
from .models import EquipoModel

class EquipoForm(forms.ModelForm):
    class Meta:
        model = EquipoModel
        fields = '__all__'
        labels = {
            'sede' : 'Sede',
            'area' : 'Area',
            'nombre' : 'Nombre',
            'procesador' : 'Procesador',
            'ram' : 'RAM',
            'almacenamiento' : 'Almacenamiento',
            'monitor' : 'Monitor',
            'teclado' : 'Teclado',
            'mouse' : 'Mouse',
            'printer1' : 'Impresora',
            'printer2' : 'Impresora'

        }
        widgets = {
            'sede' : forms.Select(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'area' : forms.Select(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'nombre' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'procesador' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'ram' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'almacenamiento' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'monitor' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'teclado' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'mouse' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'printer1' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            ),
            'printer2' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese el Area'
                }
            )
        }
