from django.urls import path
from .views import ProductPage

urlpatterns = [
    path('',ProductPage.as_view(),name='products'), 
]

