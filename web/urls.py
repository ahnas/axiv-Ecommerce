from django.urls import path
from . import views

from web.views import SearchResultsView

app_name = 'web'

urlpatterns = [ 
    path('', views.index,name="index"), 
    path('about/', views.about,name="about"), 
    path('service/', views.service,name="service"),
    path('product/', views.product,name="product"), 
    path('productsingle/<str:slug>/', views.productsingle,name="productsingle"),
    path('project/', views.project,name="project"),
    path('uproject/', views.uproject,name="uproject"), 
    path('blog/', views.blog,name="blog"), 
    path('blogsingle/<str:slug>/', views.blogsingle,name="blogsingle"),
    path('contact/', views.contact,name="contact"), 
    path('cart/', views.cart,name="cart"),
    path('checkout/', views.checkout,name="checkout"),
    path('confirmcheckout/', views.confirmcheckout,name="confirmcheckout"),  
    
    path('subscriber/', views.subscriber,name="subscriber"),
    path('feedback/', views.feedback,name="feedback"),

    path('search', SearchResultsView.as_view(), name='search_results'),


]