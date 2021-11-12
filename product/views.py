from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

from product.models import Product, ProductCate, ProductImage
# Create your views here.

class ProductPage(View):

    def get(self,request):
        product_cates = ProductCate.objects.all()
        products = Product.objects.all()
        context = {"product_cates" : product_cates,"products":products}
        return render(request,'products.html',context)

class ProductCatePage(View):

    def get(self,request,id):
        products = Product.objects.filter(category = id)
        product_cates = ProductCate.objects.all()
        category = ProductCate.objects.get(pk=id)
        context = {"product_cates" : product_cates,"products":products,"category":category}
        return render(request,'product_cate.html',context)
class ProductDetail(View):

    def get(self,request,id):
        product = Product.objects.get(pk=id)
        # products = Product.objects.all()
        related_products = Product.objects.filter(category = product.category)
        images = ProductImage.objects.filter(product = product)
        context = {"product" : product,"related_products" : related_products,"images" : images}
        return render(request,'product-detail.html',context)