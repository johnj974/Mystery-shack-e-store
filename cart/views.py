from django.shortcuts import render, redirect, reverse
from products.models import Product
# Create your views here.


def cart(request):
    return render(request, 'cart.html')


def view_cart(request):
    return render(request, "cart.html")


# add a quantity to our product
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('products'))


# adjust the quantity of a specified product
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

