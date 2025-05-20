from django.contrib import admin
from .models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Store, StoreAdmin)