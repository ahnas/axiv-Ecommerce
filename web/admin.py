from django.contrib import admin
from .models import ProductCategory,Product,Blog,Contact,Partner,Testimonial,Project,Slider,Director,ServiceEnquiry,CompletedProject,ProjectCategory

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Contact)
admin.site.register(Partner)
admin.site.register(Testimonial)
admin.site.register(Project)
admin.site.register(Slider)
admin.site.register(Director)
admin.site.register(ServiceEnquiry)
admin.site.register(ProjectCategory)
admin.site.register(CompletedProject)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}
