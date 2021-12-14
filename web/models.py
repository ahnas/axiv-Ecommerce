from django.db import models
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from uuid import uuid4
from versatileimagefield.fields import VersatileImageField,PPOIField
from django.urls import reverse


class Slider(models.Model):
    order = models.IntegerField(unique=True)
    name = models.CharField(max_length=120)
    photo = VersatileImageField(upload_to="Slider/")

    def __str__(self):
        return str(self.name)

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    productcategory = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    brochure = models.FileField(upload_to ='brochure/')
    slug = models.SlugField(unique=True)
    price = models.CharField(max_length=128)
    details = models.TextField()
    is_dashboard = models.BooleanField(default=False)
    photo = VersatileImageField(upload_to="Product/")

    
    photoOne = VersatileImageField(upload_to="Product/")
    photoTwo = VersatileImageField(upload_to="Product/")
    photoThree = VersatileImageField(upload_to="Product/")
    
    

    def get_absolute_url(self):
        return reverse('web:productsingle', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.name)



class Blog(models.Model):
    
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    photo = VersatileImageField(upload_to="Blog/")
    details = models.TextField()

    def get_absolute_url(self):
        return reverse('web:blogsingle', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    photo = VersatileImageField(upload_to="Testimonial/")
    details = models.TextField()

    def __str__(self):
        return str(self.name)


class Partner(models.Model):
    name = models.CharField(max_length=120)
    photo = VersatileImageField(upload_to="Partner/")

    class Meta:
        verbose_name = ('Sister Concern')
        verbose_name_plural = ('Sister Concerns')

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    name = models.CharField(max_length=120)
    photo = VersatileImageField(upload_to="Project/")
    details = models.TextField()

    def __str__(self):
        return str(self.name)


class Director(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    photo = VersatileImageField(upload_to="Testimonial/")
    

    def __str__(self):
        return str(self.name)




