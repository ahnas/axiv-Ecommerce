import django
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Cart
from django.forms.models import model_to_dict
# Create your views here.

def addToCart(request):
    sessionID = request.session.session_key
    pid = request.POST['product_id']

    checkCart = Cart.objects.filter(session_key = sessionID,product_id = pid )
    if checkCart.exists():
        msg = '1'
    else:
            saveCart = Cart()
            saveCart.session_key = sessionID
            saveCart.product_id = pid
            saveCart.quantity = 1
            saveCart.save()
            msg = '0'
    cartLength = Cart.objects.filter(session_key = sessionID).count()

    context = {
            "cartLength" : cartLength,
            "msg":msg   
        }

    return JsonResponse(context)


def headerloader(request):
    sessionID = request.session.session_key
    cartLength = Cart.objects.filter(session_key = sessionID).count()
    context = {
            "cartLength" : cartLength,
        }
    return JsonResponse(context)


def updatecart(request): 
    sessionID = request.session.session_key
    
    productId = request.POST['productID']
    qty = request.POST['qty']

    if Cart.objects.filter(session_key = sessionID,product_id= productId ).exists():
        instance = Cart.objects.get(session_key = sessionID,product_id= productId )
        instance.quantity = qty
        instance.save()
    subtotal = 0
    cartItems = Cart.objects.filter(session_key = sessionID)
    for cartItem in cartItems:subtotal += cartItem.quantity*cartItem.product.price
    productPrice = int(instance.quantity)*int(instance.product.price)
    context={
        "productPrice":productPrice,
        "subtotal":subtotal

    }

    return JsonResponse(context)
