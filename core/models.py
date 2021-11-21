
from django.db import models
from ckeditor.fields import RichTextField
 
class Banner(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    def __str__(self) -> str:
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=200)
    video = models.CharField(max_length=200,null=True)
    def __str__(self) -> str:
        return self.name
 
class Service(models.Model):
    logo = models.ImageField()
    web_title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    map = models.CharField(max_length=1000)
    facebook = models.CharField(max_length=1000)
    youtube = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    open_time = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    abus = models.CharField(max_length=300, null=True)
    abus_title = models.CharField(max_length=300, null=True)
    abus_content = RichTextField(null=True)
    abus_image = models.ImageField(null=True)
    def __str__(self) -> str:
        return self.web_title
 

class ShopService(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(null=True)
    
    def __str__(self) -> str:
        return self.name

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Reviewer(models.Model):
    name = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)
    comment = models.TextField(max_length=1000, null=True)
    avatar = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name
