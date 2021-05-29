from django.urls import path, include
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductDeleteView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'), 
]