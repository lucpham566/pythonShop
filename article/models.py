from django.db import models
import datetime
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class NewCate(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class New(models.Model):
    category = models.ForeignKey(NewCate, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    avatar = models.ImageField(null=True)
    content = RichTextField(null=True)
    special = models.BooleanField(default=True)
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.title