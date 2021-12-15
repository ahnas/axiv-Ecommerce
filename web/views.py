from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json 
from .models import CompletedProject, Partner, ProductCategory,Product,Blog, Project, ProjectCategory,Testimonial,Slider,Director
from .forms import ContactForm,ServiceEnquiryForm

def index(request):
    projectcategory = ProjectCategory.objects.all()
    project =CompletedProject.objects.all()
    slider = Slider.objects.all()
    blog = Blog.objects.filter().order_by('-id')[:3]
    product = Product.objects.filter(is_dashboard = True)
    partner = Partner.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "is_index" : True,
        "product":product, 
        "partner":partner,
        "testimonial":testimonial,
        "slider":slider,
        "blog":blog,
        "projectcategory":projectcategory,
        "project":project,
    }
    return render(request, 'index.html',context)

def about(request): 
    director = Director.objects.all()
    context = {
        "is_about" : True,
        "director":director,
    }
    return render(request, 'about.html',context)

def service(request):
    form = ServiceEnquiryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Contact You Soon"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_service" : True ,
            "form":form,
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
    category =  Product.objects.get(slug = slug)
    getCategory = category.productcategory.id
    similiarproduct = Product.objects.filter(productcategory_id = getCategory).exclude(slug = slug)
    product = get_object_or_404(Product, slug=slug)
    context = {
        "is_productsingle" : True,
        "product":product,
        "similiarproduct":similiarproduct,
    }
    for i in similiarproduct:
        print(i)
    return render(request, 'productsingle.html',context)

def project(request):
    context = {
        "is_project" : True
    }
    return render(request, 'project.html',context) 

def uproject(request):
    project = Project.objects.all()
    context = {
        "is_uproject" : True,
        "project":project,
    }
    return render(request, 'uproject.html',context) 

def blog(request):
    blog = Blog.objects.filter().order_by('-date')
    context = {
        "is_blog" : True,
        "blog":blog,
    }
    return render(request, 'blog.html',context) 

def blogsingle(request,slug):
    similiarblog = Blog.objects.all().exclude(slug = slug)
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        "is_blogsingle" : True,
        "blog":blog,
        "similiarblog":similiarblog,
    }
    for i in similiarblog:
        print(i)
    return render(request, 'blogsingle.html',context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Message successfully updated"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact" : True,
            "form":form,
        }
    return render(request, 'contact.html',context)

def cart(request):
    context = {
            "is_cart" : True,
            
        }
    return render(request, 'cart.html',context)
