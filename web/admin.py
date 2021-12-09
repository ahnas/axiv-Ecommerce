from django.contrib import admin
from .models import ProductCategory,Product,Blog,Contact,Partner,Testimonial

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Contact)
admin.site.register(Partner)
admin.site.register(Testimonial)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}
