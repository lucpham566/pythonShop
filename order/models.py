from django.db import models

from cart.models import Cart, Customer

# Create your models here.


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    date = models.DateTimeField(default=0)
    def __str__(self) -> str:
        return self.customer.name