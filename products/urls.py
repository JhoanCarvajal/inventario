from django.urls import path, include
from .views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'), 
]