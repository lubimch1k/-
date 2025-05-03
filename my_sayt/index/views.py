from django.shortcuts import render
from .models import Category, Product
# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.app()

    context = {
        'categories': categories, 'products': products,
    }
    return render(request, "home.html", context)

