from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json 
from .models import Partner, ProductCategory,Product,Blog, Project,Testimonial,Slider,Director
from .forms import ContactForm

def index(request):
    slider = Slider.objects.all()


    class slide:
        def __init__(self,id,order,name,photo) :
            self.id = id
            self.order = order
            self.photo = photo
            self.name = name.split(' ')
    sliders = []
    for s in slider:
        sliders.append(slide(s.id,s.order,s.name,s.photo))
        

    blog = Blog.objects.filter().order_by('-id')[:3]
    product = Product.objects.filter(is_dashboard = True)
    partner = Partner.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "is_index" : True,
        "product":product, 
        "partner":partner,
        "testimonial":testimonial,
        "sliders":sliders,
        "blog":blog,
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
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        "is_blogsingle" : True,
        "blog":blog,
    }
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
