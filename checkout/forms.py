from django import forms
from .models import Order


# payment form for customer
class PaymentForm(forms.Form):
    MONTH_CHOICES = [(m, m) for m in range(1, 12)]
    YEAR_CHOICES = [(y, y) for y in range(2020, 2030)]
    credit_card_number = forms.CharField(label='Card number', required=False)
    cvv = forms.CharField(label='Security code', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address1', 'address2', 'town_or_city', 'county', 'eir_code', 'contact_number')