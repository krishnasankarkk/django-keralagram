from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm

def login_view(request):
    if request.method == "POST":
       form = LoginForm(request, data=request.POST)
       
       if form.is_valid():
           username = request.POST["username"]
           password = request.POST["password"]
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
           else:
               form.add_error(None, 'Invalid username or passwprd!')
    else:
        form = LoginForm()
        
    context = {"form":form}
    return render(request, "users/login.html", context)

def signup(request):
    form = RegistrationForm()
    context = {"form":form}
    return render(request, "users/signup.html", context)

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def profile(request):
    return render(request, "users/profile.html")

def create(request):
    return render(request, "base.html")
