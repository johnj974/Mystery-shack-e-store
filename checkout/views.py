from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
# this ensures customer is logged in before they can proceed to checkout
from django.contrib.auth.decorators import login_required
# forms imported for use in our views
from .forms import PaymentForm, OrderForm
# used to confirm payment
import stripe
# import machinery class to be used
from products.models import Machinery
# to create a timestamp when order is placed
from django.utils import timezone
# to provide a visible message to the user
from django.contrib import messages
# class to be used in view
from .models import OrderItem

stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save
        cart = request.session.get('cart',{})
        total = 0
        for id, quantity in cart.items():
            product = get_object_or_404(Machinery, pk=id)
            total += quantity * product.price
            order_item = OrderItem(
                order=order,
                product=product,
                quantity=quantity
            )
            order_item.save()
    
        try:
            customer = stripe.Charge.create(
                amount = int(total * 100),
                currency = "EUR",
                description = request.user.email,
                card = payment_form.cleaned_data['stripe_id'],
            )
        except stripe.error.CardError:
            messages.error(request, "You card was declined")
        if customer.paid:
            messages.error(request, "Payment has been accepted")
            request.session["cart"] = {}
            return redirect(reverse("products"))