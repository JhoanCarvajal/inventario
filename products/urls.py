from django.urls import path, include
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'), 
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'), 
]