from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
