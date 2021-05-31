from django import forms
from django.forms import widgets
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['nombre', 'precio', 'informacion', 'fecha_adquisicion', 'imagen', 'id_usuario']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nombre', 'imagen', 'precio', 'informacion', 'fecha_adquisicion']

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            # 'imagen':forms.FileInput(attrs={'class':'form-control', 'style':'height: 70px; padding-top: 38px;', 'placeholder':'Imagen'}),
            'precio':forms.NumberInput(attrs={'class':'form-control', 'min':'1000', 'placeholder':'Precio'}),
            'informacion':forms.Textarea(attrs={'class':'form-control', 'style':'height: 100px;', 'placeholder':'Informacion'}),
            'fecha_adquisicion':forms.DateInput(format ='%Y-%m-%d', attrs={'type':'date','class':'form-control', 'placeholder':'Fecha de adquisicion'}),
        }
        labels = {
            'nombre':'Nombre',
            'imagen':'Imagen',
            'precio':'Precio',
            'informacion':'Informacion',
            'fecha_adquisicion':'Fecha de adquisicion',
        }

