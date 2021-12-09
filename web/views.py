from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json 
from .models import ProductCategory,Product


def index(request):
    context = {
        "is_index" : True 
    }
    return render(request, 'index.html',context)

def about(request): 
    context = {
        "is_about" : True
    }
    return render(request, 'about.html',context)

def service(request):
    context = {
        "is_service" : True 
    }
    return render(request, 'service.html',context)

def product(request):
    productcategory = ProductCategory.objects.all()
    product = Product.objects.all()
    context = {
        "is_product" : True ,
        "productcategory":productcategory,
        "product":product,
    }
    return render(request, 'product.html',context)

def productsingle(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        "is_productsingle" : True,
        "product":product,
    }
    return render(request, 'productsingle.html',context)

def project(request):
    context = {
        "is_project" : True
    }
    return render(request, 'project.html',context) 

def uproject(request):
    context = {
        "is_uproject" : True
    }
    return render(request, 'uproject.html',context) 

def blog(request):
    context = {
        "is_blog" : True
    }
    return render(request, 'blog.html',context) 

def blogsingle(request):
    context = {
        "is_blogsingle" : True
    }
    return render(request, 'blogsingle.html',context)

def contact(request):
    context = {
        "is_contact" : True
    }
    return render(request, 'contact.html',context)
