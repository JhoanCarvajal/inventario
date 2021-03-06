from django.shortcuts import render
from django.http import request 
# ccb
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Product
from .forms import ProductForm, ProductUpdateForm

# Create your views here.

# listar los productos
@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    def get_queryset(self):
        return Product.objects.filter(id_user=self.request.user)


# ver cada producto individual
@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product


# crear un producto nuevo
@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse_lazy('product_list')


# actualizar un producto
@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('product_list')


# eliminar un producto
@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
