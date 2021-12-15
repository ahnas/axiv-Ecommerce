from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Cart

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
