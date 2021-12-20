from django.contrib import admin
from .models import ProductCategory,Product,Blog,Contact,Partner,Testimonial,Project,Slider,Director,ServiceEnquiry,CompletedProject,ProjectCategory,Certification,Email,Service,Feedback

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Certification)
admin.site.register(Contact)
admin.site.register(Partner)
admin.site.register(Testimonial)
admin.site.register(Project)
admin.site.register(Slider)
admin.site.register(Director)
admin.site.register(ServiceEnquiry)
admin.site.register(ProjectCategory)
admin.site.register(CompletedProject)
admin.site.register(Email)
admin.site.register(Service)
admin.site.register(Feedback)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}
