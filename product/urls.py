from django.urls import path

from .views import ProductCatePage, ProductDetail, ProductPage 
from .views import *
urlpatterns = [
    path('',ProductPage.as_view(),name='products'), 
    path('cate/<int:id>',ProductCatePage.as_view(),name='product-cate'), 
    path('detail/<int:id>',ProductDetail.as_view(),name='product-detail'), 
    path('comment-product',addComment,name='comment-product'), 
]

