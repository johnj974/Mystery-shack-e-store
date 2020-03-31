from django.shortcuts import render
# this ensures customer is logged in before they can proceed to checkout
from django.contrib.auth.decorators import login_required
# forms imported for use in our views
from .forms import PaymentForm, OrderForm
# used to confirm payment
# import stripe


def checkout(request):
    return render(request, 'checkout.html')