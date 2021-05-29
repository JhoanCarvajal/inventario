from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['nombre', 'imagen', 'precio', 'informacion', 'fecha_adquisicion']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
