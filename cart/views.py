from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from cart.form import SendCheckout
from cart.models import Cart, CartItem, Customer
from order.models import Bill
import datetime

from product.models import Product

# Create your views here.

class Checkout(View):
    def get(self,request):
        
        form = SendCheckout()
        cart = request.session.get('cart')
        total = 0
        for item in cart:
            total = int(total) + int(cart[item]['total'])
        
        context = {"cart" : cart,"total" : total,'form': form}
        if  request.session.get('checkout_success'):
            request.session['checkout_success']=False
            context['checkout_success']=True
            return render(request,'order.html',context)
        return render(request,'order.html',context)


def addToCart(request):
    cart=request.session.get('cart') if request.session.get('cart') else {}
    if True:
        id = request.GET.get('id')
        num = request.GET.get('num')
        product = Product.objects.get(pk=id)
        
        if id in cart.keys():
            itemCart = {
                'name' : product.name,
                'price' : product.price,
                'image' : product.avatar.url if product.avatar else "",
                'quantity' : int(cart[id]['quantity']) + int(num)
            }
        else :
            itemCart = {
                'name' : product.name,
                'price' : product.price,
                'image' : product.avatar.url if product.avatar else "",
                'quantity' : 1
            }
        itemCart['total'] = int(itemCart['price'])*int(itemCart['quantity'])
        cart[id]= itemCart
        request.session['cart'] = cart

    return JsonResponse({"success":"thành công","total":len(cart)})

def removeToCart(request):
    cart=request.session.get('cart') if request.session.get('cart') else {}
    if True:
        if request.is_ajax():
            id = request.GET.get('id')
            # num = request.GET.get('num')
            
            cart.pop(id)
            request.session['cart'] = cart
            # return HttpResponse('oke')
            total_price = 0
            for item in cart:
                total_price = int(total_price) + int(cart[item]['total'])
            
    
            
    return JsonResponse({"success":"xóa thành công", "total":len(cart), "total_price":total_price})


def process(request):
    # return HttpResponse(request.method)
    if request.method == "POST":
        cart=request.session.get('cart') if request.session.get('cart') else {}

        name = request.POST.get('name')
        email =request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        customer = Customer.objects.create(name=name,email=email,address=address,phone=phone)
        customer.save()

        newCart = Cart.objects.create(customer=customer)
        newCart.save()
        for item in cart:
            product = Product.objects.get(pk=item)
            cartItem = CartItem.objects.create(cart=newCart,item=product,quantity=cart[item]['quantity'])
            cartItem.save()

        total = 0
        for item in cart:
            total = int(total) + int(cart[item]['total'])

        bill = Bill.objects.create(customer=customer,cart=newCart,total=total,date=datetime.datetime.now())
        bill.save()

        request.session['checkout_success']=True

        return redirect("checkout")
    else:
        return HttpResponse("khong phai post method")