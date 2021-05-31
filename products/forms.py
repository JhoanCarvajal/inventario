from django import forms
from django.forms import widgets
from .models import Product


# form para registrar un producto
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'information', 'acquisition_date', 'image', 'id_user']


# form para actualizar un producto
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'information', 'acquisition_date']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            # 'image':forms.FileInput(attrs={'class':'form-control', 'style':'height: 70px; padding-top: 38px;', 'placeholder':'Imagen'}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'min':'1000', 'placeholder':'Precio'}),
            'information':forms.Textarea(attrs={'class':'form-control', 'style':'height: 100px;', 'placeholder':'Informacion'}),
            'acquisition_date':forms.DateInput(format ='%Y-%m-%d', attrs={'type':'date','class':'form-control', 'placeholder':'Fecha de adquisicion'}),
        }
        labels = {
            'name':'Nombre',
            'image':'Imagen',
            'price':'Precio',
            'information':'Información',
            'acquisition_date':'Fecha de adquisición',
        }

