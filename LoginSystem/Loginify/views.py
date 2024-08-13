from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import LoginForm,SignupForm


def index(request):
    return render(request, 'Loginify/index.html')


def signup(request):
    # form = SignupForm()
    # return render(request, 'Loginify/signup.html', {'form': form})

    # # return HttpResponse('Hello World Sign UP')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else :
        form = SignupForm()
        return render(request, 'Loginify/signup.html', {'form': form})
    return render(request, 'Loginify/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle the login logic here
            return redirect('/')
    else:
        form = LoginForm()

    # form = LoginForm()
    return render(request, 'Loginify/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('Loginify:login')