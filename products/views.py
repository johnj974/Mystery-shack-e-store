from django.shortcuts import render, redirect, reverse, get_object_or_404
# import the machinery object from models so we can render to our view
from .models import Product
from .forms import ProductForm
# import to restrict users accessing create/update/delete functionallity from the url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound


# view to render to machinery.html
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# create product view
@login_required
def createProduct(request):
    form = ProductForm()
    if request.user.is_superuser:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('products'))
        context = {'form': form}
        return render(request, "product_form.html", context)
    else:
        return HttpResponseNotFound('<h1>Unauthorised Action, Please return to your previous page, you have 5 seconds to comply!</h1>')
   


@login_required
def updateProduct(request, id):
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=id)
        form = ProductForm(instance=product)

        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect(reverse('products'))

        context = {'form': form}
        return render(request, "product_form.html", context)
    else:
        return HttpResponseNotFound('<h1>Unauthorised Action, Please return to your previous page, you have 5 seconds to comply!!</h1>') 

@login_required
def deleteProduct(request, id):
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=id)
        if request.method == "POST":
            product.delete()
            return redirect(reverse('products'))
        context = {'item': product}
        return render(request, "delete.html", context)
    else:
        return HttpResponseNotFound('<h1>Unauthorised Action, Please return to your previous page, you have 5 seconds to comply!!!</h1>') 