from django.shortcuts import render


# function request to render index page
def index(request):
    return render(request, 'index.html')
