from django.shortcuts import render
from .models import Sale

# Create your views here.
def sale(request):
    sales = Sale.objects.select_related('store', 'product')
    context = {
        'sales':sales,
    }
    return render(request, "sale/sale.html", context)