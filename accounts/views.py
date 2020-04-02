# reverse, redirect added to existing library
from django.shortcuts import render, reverse, redirect
# additional django library with ability to show messages
from django.contrib import auth, messages
# forms imported from forms.py file
from accounts.forms import LoginForm, UserRegistrationForm
# additional library to stop unauthorised use of functions
from django.contrib.auth.decorators import login_required
# importing user model
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


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
        login_form = LoginForm(request.POST)
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
        login_form = LoginForm()    # creates an instance of the form
    return render(request, 'login.html', {'login_form': login_form})    # form passed in for rendering to page


# function for registration
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


# user profile view
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})


"""def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            raw_password = registration_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('register')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'index.html', {'form': registration_form})"""