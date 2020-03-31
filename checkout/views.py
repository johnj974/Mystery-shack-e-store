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
    return render(request, 'checkout.html')