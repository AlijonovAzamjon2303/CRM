from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category', 'barcode']
    autocomplete_fields = ['category', 'store']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
