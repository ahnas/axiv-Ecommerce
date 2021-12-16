from django.contrib import admin
from .models import Cart,Order,CheckOuted

# Register your models here.





@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('session_key','date','name')

@admin.register(CheckOuted)
class CheckOutedAdmin(admin.ModelAdmin):
    
    list_display = ('session_key','date')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    
    list_display = ('session_key','date')