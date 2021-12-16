from django.db import models
from web.models import Project,Product

# Create your models here.


class Cart(models.Model):
    date = models.DateField(auto_now_add=True)
    session_key = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

