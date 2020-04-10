from django.shortcuts import render, redirect, reverse
# import the machinery object from models so we can render to our view
from .models import Product
from .forms import ProductForm


# view to render to machinery.html
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# create product view
def createProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))
    context = {'form': form}
    return render(request, "product_form.html", context)


def updateProduct(request, id):
    form = ProductForm()
    context = {'form': form}
    return render(request, "product_form.html", context)
