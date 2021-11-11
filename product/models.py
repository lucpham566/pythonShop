from django.db import models

 
class ProductCate(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
 
class Product(models.Model):
    category = models.ForeignKey(ProductCate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    intro = models.CharField(max_length=300)
    content = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return self.name

