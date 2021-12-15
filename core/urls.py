from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [  
    path('addToCart/', views.addToCart,name="addToCart"), 
    path('headerloader/', views.headerloader,name="headerloader"), 
]
    