from django.db import models

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
    content = models.TextField(max_length=5000, null=True)
    special = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title