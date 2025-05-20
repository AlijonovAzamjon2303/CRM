from django.db.models.signals import post_init
from django.shortcuts import render
from .models import Product

# Create your views here.
def info(request):
    products = Product.objects.select_related('category', 'store')
    print(products)
    context = {
        'name':"A'zamjon",
        'fam': "Alijonov",
        'products':products
    }
    return render(request, "product/index.html", context)