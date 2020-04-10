from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))

    context = {'form': form}
    return render(request, "product_form.html", context)
