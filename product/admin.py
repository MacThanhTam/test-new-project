from django.contrib import admin
# from product.models import Product, Category

# from django.contrib import admin
from .models import Category, Product, ProductImage
from unidecode import unidecode
# from .form import ProductAdminForm


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}
admin.site.register(Category, CategoryAdmin)
# class PhotoInline(admin.StackedInline):
#     model = ProductImage
#     extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','category_id','image','price', 'active', 
                    'quantity', 'author', 'ISBM','publish','publisher','status','page_number','cover_type','size']
    prepopulated_fields = {'slug': ('title',)}
    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.product.create(image=afile)

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProductImage, ProductImageAdmin)

