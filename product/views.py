from django.shortcuts import render
from django.views import View

from product.models import Product, ProductCate
# Create your views here.

class ProductPage(View):

    def get(self,request):
        product_cates = ProductCate.objects.all()
        products = Product.objects.all()
        context = {"product_cates" : product_cates,"products":products}
        return render(request,'products.html',context)