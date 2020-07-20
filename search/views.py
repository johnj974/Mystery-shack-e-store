from django.shortcuts import render
# import the machinery object from models so we can render to our view
from products.models import Product
# from django.contrib import auth, messages


# a search function to search for items
def search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {'products': products})
