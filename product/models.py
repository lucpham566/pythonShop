from django.db import models
import datetime


 
class ProductCate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,null=True)
    video = models.CharField(max_length=500,null=True)
    def __str__(self) -> str:
        return self.name
 
class Product(models.Model):
    category = models.ForeignKey(ProductCate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    avatar = models.ImageField(null=True)
    price = models.IntegerField(default=0)
    vote = models.IntegerField(default=5)
    intro = models.TextField(max_length=300)
    content = models.TextField(max_length=5000)
    special = models.BooleanField(default=True)
    status = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    warranty_time = models.CharField(max_length=100, null=True)
    def __str__(self) -> str:
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    def __str__(self) -> str:
        return self.product.name



class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    vote = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.now)
    
    def __str__(self) -> str:
        return self.name
