from django.contrib import admin

from cart.models import CartItem, Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(CartItem)
