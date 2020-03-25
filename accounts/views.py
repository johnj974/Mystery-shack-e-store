# reverse, redirect added to existing library
from django.shortcuts import render, reverse, redirect
# additional django library
from django.contrib import auth, messages
# form imported from forms.py file
from accounts.forms import loginForm
# additional library to stop unauthorised use of functions
from django.contrib.auth.decorators import login_required


# function to render index page
def index(request):
    return render(request, 'index.html')


# function to activate logout/logout user
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successfull")
    return redirect(reverse('index'))


# login function with django forms
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = loginForm()
    return render(request, 'login.html', {'login_form': login_form})    # form passed in for rendering to page


# function for registration
def register(request):
    return render(request, 'register.html')
