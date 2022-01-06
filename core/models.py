from django.db import models
from web.models import Project,Product

# Create your models here.


class Cart(models.Model):
    date = models.DateField(auto_now_add=True)
    session_key = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class CheckOuted(models.Model):
    date = models.DateField(auto_now_add=True)
    session_key = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10)



class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=1000)
    number = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)

    session_key = models.CharField(max_length=1000)



    def __str__(self):
        return self.name 

