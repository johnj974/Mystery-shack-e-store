from django.shortcuts import render
from .models import RareItem
# Create your views here.


def rare_items(request):
    rare = RareItem.objects.all()
    return render(request, 'rare_items.html', {'rare': rare})
