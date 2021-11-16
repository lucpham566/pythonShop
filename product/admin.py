
from django.contrib import admin
from .models import Comment, Product,ProductCate, ProductImage
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCate)
admin.site.register(ProductImage)
admin.site.register(Comment)