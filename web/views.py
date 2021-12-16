from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
import datetime
from core.models import Cart, Order, CheckOuted
from .models import CompletedProject, Partner, ProductCategory, Product, Blog, Project, ProjectCategory, Testimonial, Slider, Director
from .forms import ContactForm, ServiceEnquiryForm, OrderForm


def index(request):
    if request.session.session_key == None:
        request.session.create()
        request.session['axiva'] = 'initilise'

    projectcategory = ProjectCategory.objects.all()
    project = CompletedProject.objects.all()
    slider = Slider.objects.all()
    blog = Blog.objects.filter().order_by('-id')[:3]
    product = Product.objects.filter(is_dashboard=True)
    partner = Partner.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "is_index": True,
        "product": product,
        "partner": partner,
        "testimonial": testimonial,
        "slider": slider,
        "blog": blog,
        "projectcategory": projectcategory,
        "project": project,
    }
    return render(request, 'index.html', context)


def about(request):
    if request.session.session_key == None:
        request.session.create()
        request.session['axiva'] = 'initilise'

    director = Director.objects.all()
    context = {
        "is_about": True,
        "director": director,
    }
    return render(request, 'about.html', context)


def service(request):
    form = ServiceEnquiryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Contact You Soon"
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_service": True,
            "form": form,
        }
    return render(request, 'service.html', context)


def product(request):
    if request.session.session_key == None:
        request.session.create()
        request.session['axiva'] = 'initilise'

    productcategory = ProductCategory.objects.all()
    product = Product.objects.all()
    context = {
        "is_product": True,
        "productcategory": productcategory,
        "product": product,
    }
    return render(request, 'product.html', context)


def productsingle(request, slug):
    if request.session.session_key == None:
        request.session.create()
        request.session['axiva'] = 'initilise'

    category = Product.objects.get(slug=slug)
    getCategory = category.productcategory.id
    similiarproduct = Product.objects.filter(
        productcategory_id=getCategory).exclude(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    context = {
        "is_productsingle": True,
        "product": product,
        "similiarproduct": similiarproduct,
    }
    for i in similiarproduct:
        print(i)
    return render(request, 'productsingle.html', context)


def project(request):
    context = {
        "is_project": True
    }
    return render(request, 'project.html', context)


def uproject(request):
    project = Project.objects.all()
    context = {
        "is_uproject": True,
        "project": project,
    }
    return render(request, 'uproject.html', context)


def blog(request):
    blog = Blog.objects.filter().order_by('-date')
    context = {
        "is_blog": True,
        "blog": blog,
    }
    return render(request, 'blog.html', context)


def blogsingle(request, slug):
    similiarblog = Blog.objects.all().exclude(slug=slug)
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        "is_blogsingle": True,
        "blog": blog,
        "similiarblog": similiarblog,
    }
    for i in similiarblog:
        print(i)
    return render(request, 'blogsingle.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated"
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, 'contact.html', context)


def cart(request):
    sessionID = request.session.session_key
    cartItem = Cart.objects.filter(session_key=sessionID)

    class cart:
        def __init__(self, cnt, product, quantity, price):
            self.cnt = cnt
            self.product = product
            self.quantity = quantity
            self.price = price
    cartItems = []
    totalprice = 0
    if Cart.objects.filter(session_key=sessionID).exists():
        cnt = 1

        for item in cartItem:
            totalprice += int(item.quantity)*int(item.product.price)
            cartItems.append(cart(cnt, item.product, item.quantity,
                             int(item.quantity)*int(item.product.price)))
            cnt += 1

    context = {
        "is_cart": True,
        "cartItems": cartItems,
        "totalprice": totalprice
    }
    return render(request, 'cart.html', context)


def checkout(request):
    form = OrderForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        number = request.POST.get('number')
        if Order.objects.filter(session_key = request.session.session_key).exists():
            getOrder = Order.objects.get(session_key = request.session.session_key)
            getOrder.name = name
            getOrder.address = address
            getOrder.number = number
            getOrder.date = datetime.datetime.now()
            getOrder.save()
            orderID = getOrder.id
            date = getOrder.date
        else:
            orderSave = Order()
            orderSave.name = name
            orderSave.address = address
            orderSave.number = number
            orderSave.session_key = request.session.session_key
            orderSave.save()
            orderID = orderSave.id
            date = orderSave.date
        cartitems = Cart.objects.filter(
            session_key=request.session.session_key)
        cartitems1 = Cart.objects.filter(
            session_key=request.session.session_key)

        class cart:
            def __init__(self, cnt, product, quantity, price):
                self.product = product
                self.cnt = cnt
                self.quantity = quantity
                self.price = price
        cartItems = []
        totalprice = 0
        messagestring=''
        if Cart.objects.filter(session_key=request.session.session_key).exists():
            cnt = 1
            for item in cartitems1:
                totalprice += int(item.quantity)*int(item.product.price)
                cartItems.append(cart(cnt, item.product, item.quantity,
                                      int(item.quantity)*int(item.product.price)))
                cnt += 1

            messagestring = 'https://wa.me/+919562540226?text=Name :'+name+'%0aAddress :'+address+'%0aPhone :'+number +\
                "%0a-----Order Details------"

            for cartItem in cartItems:
                messagestring += "%0aProduct-Id:"+str(cartItem.product.id)+"%0aName:"+str(cartItem.product.name)+"%0aQty:"+str(
                    cartItem.quantity)+"%0aPrice:"+str(cartItem.product.price)+"%0aTotal :"+str(cartItem.price)+"%0a-----------------------------"
            messagestring += "%0a-----------------------------%0a\
            Grand Total :"+str(totalprice)+"%0a--------------------------------"       

        

        userDetails = {
            'name':  name,
            'address':  address,
            'number':  number,
            'orderID':  orderID,
            'date': date,
        }

        return render(request, 'checkout.html', {"messagestring":messagestring,"totalprice": totalprice, "cartitems": cartItems, "form": form, "invoice": True, "userDetails": userDetails})
    return render(request, 'checkout.html', {"form": form, "invoice": False})


def confirmcheckout(request):
    cartitems = Cart.objects.filter(session_key=request.session.session_key)
    for items in cartitems:
        checkout = CheckOuted()
        checkout.date = items.date
        checkout.session_key = items.session_key
        checkout.product = items.product
        checkout.quantity = items.quantity
        checkout.status = 'open'
        checkout.save()

    Cart.objects.filter(session_key=request.session.session_key).delete()
    return JsonResponse({"success": "yes"})
