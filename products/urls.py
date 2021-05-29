from django.urls import path, include
from .views import ProductCreateView, ProductListView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'), 
]