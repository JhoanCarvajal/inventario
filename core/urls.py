from django.urls import path, include
from .views import LandingPageView, ReporteExcel

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'), 
    path('excel/', ReporteExcel.as_view(), name='excel')
]