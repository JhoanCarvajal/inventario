from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['nombre', 'precio', 'informacion', 'fecha_adquisicion', 'imagen', 'id_usuario']