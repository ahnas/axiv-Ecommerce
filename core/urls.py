from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [  
    path('addToCart/', views.addToCart,name="addToCart"), 
    path('headerloader/', views.headerloader,name="headerloader"), 
    path('updatecart/', views.updatecart,name="updatecart"),
    path('deleteCart/', views.deleteCart,name="deleteCart"),
    path('addOrUpdate/', views.addOrUpdate,name="addOrUpdate"),

]
    