# reverse, redirect added to existing library
from django.shortcuts import render, reverse, redirect
# additional django library
from django.contrib import auth, messages


# function to render index page
def index(request):
    return render(request, 'index.html')


# function to activate logout/logout user
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successfull")
    return redirect(reverse('index'))

