from django.shortcuts import render
# import the machinery object from models so we can render to our view
from .models import Product


# view to render to machinery.html
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

"""
# a search function to search for items
def search(request):
    products = Product.objects.filter(name_icontains=request.GET['q'])
    return render(request, 'products.html', {'products': products})"""



