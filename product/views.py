from django.http.response import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import View

from product.models import Comment, Product, ProductCate, ProductImage
# Create your views here.

class ProductPage(View):

    def get(self,request):
        product_cates = ProductCate.objects.all()
        product_list = Product.objects.all()
        
        page_number = request.GET.get("page")
        if request.GET.get("product_name"):
            try:
                name=request.GET.get("product_name")
                product_list = Product.objects.filter(name__contains=name)
            except Product.DoesNotExist:
                product_list = None
            
        paginator = Paginator(product_list, 3)
        
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
            products = paginator.page(1)
        except EmptyPage:
            # Nếu page không có item nào, trả về page cuối cùng
            products = paginator.page(paginator.num_pages)

        
        context = {"product_cates" : product_cates,"products":products}
        return render(request,'products.html',context)

class ProductCatePage(View):

    def get(self,request,id):
        product_list = Product.objects.filter(category = id)
        product_cates = ProductCate.objects.all()
        category = ProductCate.objects.get(pk=id)
        
        
        page_number = request.GET.get("page")
        if request.GET.get("product_name"):
            try:
                name=request.GET.get("product_name")
                product_list = Product.objects.filter(category = id,name__contains=name)
            except Product.DoesNotExist:
                product_list = None
            
        paginator = Paginator(product_list, 3)
        
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
            products = paginator.page(1)
        except EmptyPage:
            # Nếu page không có item nào, trả về page cuối cùng
            products = paginator.page(paginator.num_pages)

        
        context = {"product_cates" : product_cates,"products":products,"category":category}
        return render(request,'product_cate.html',context)

class ProductDetail(View):

    def get(self,request,id):
        product = Product.objects.get(pk=id)
        # products = Product.objects.all()
        related_products = Product.objects.filter(category = product.category)
        images = ProductImage.objects.filter(product = product)
        comments = Comment.objects.filter(product = product).order_by('-id')
        context = {"product" : product,"related_products" : related_products,"images" : images,"comments" : comments}
        return render(request,'product-detail.html',context)


def addComment(request):
    
    vote = request.GET.get('vote')
    name = request.GET.get('name')
    title = request.GET.get('title')
    content = request.GET.get('content')
    product_id = request.GET.get('product_id')
    # return JsonResponse({"success":"thành công"})
    
    product = Product.objects.get(pk=product_id)
    
    comment = Comment.objects.create(product=product,name=name,vote=vote,title=title,content=content)
    comment.save()
    
    return JsonResponse({"success":"thành công", "created_at":comment.date})