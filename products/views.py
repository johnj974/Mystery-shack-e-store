from django.shortcuts import render
# import the machinery object from models so we can render to our view
from .models import Machinery


# view to render to machinery.html
def all_machinery(request):
    machinery = Machinery.objects.all()
    return render(request, 'machinery.html', {'machinery': machinery})


# a search function to search for items
def search(request):
    products = Machinery.objects.filter(name_icontains=request.GET['q'])
    return render(request, 'machinery.html', {'products':products})



