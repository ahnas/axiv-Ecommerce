from django.db import models
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from uuid import uuid4
from versatileimagefield.fields import VersatileImageField,PPOIField
from django.urls import reverse



class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    productcategory = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    price = models.CharField(max_length=128)
    details = models.TextField()

    photo = VersatileImageField(blank=True,null=True,upload_to="Product/")

    photoOne = VersatileImageField(ppoi_field='photoOne_ppoi',default='default.png',upload_to="Product/")
    photoOne_ppoi = PPOIField()

    photoTwo = VersatileImageField(ppoi_field='photoTwo_ppoi',default='default.png',upload_to="Product/")
    photoTwo_ppoi = PPOIField()

    photoThree = VersatileImageField(ppoi_field='photoThree_ppoi',default='default.png',upload_to="Product/")
    photoThree_ppoi = PPOIField()

    photoFour = VersatileImageField(ppoi_field='photoFour_ppoi',default='default.png',upload_to="Product/")
    photoFour_ppoi = PPOIField()


    def get_absolute_url(self):
        return reverse('web:productsingle', kwargs={'slug': self.slug})


    def __str__(self):
        return str(self.name)

