
from django.db import models

 
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
    def __str__(self) -> str:
        return self.web_title
 


