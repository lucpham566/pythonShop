from django.urls import path

from .views import ProductCatePage, ProductDetail, ProductPage 

urlpatterns = [
    path('',ProductPage.as_view(),name='products'), 
    path('cate/<int:id>',ProductCatePage.as_view(),name='product-cate'), 
    path('detail/<int:id>',ProductDetail.as_view(),name='product-detail'), 
]

