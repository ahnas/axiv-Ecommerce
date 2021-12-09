from django.contrib import admin
from .models import ProductCategory,Product

# Register your models here.


admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}