from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib import messages

from .forms import LoginForm, RegistrationForm
from .models import UserAccount
from posts.models import Post

def login_view(request):
    # if request.method == "POST":
    #    form = LoginForm(request, data=request.POST)
       
    #    if form.is_valid():
    #        username = request.POST["username"]
    #        password = request.POST["password"]
    #        user = authenticate(request, username=username, password=password)
    #        if user is not None:
    #            login(request, user)
    #        else:
    #            form.add_error(None, 'Invalid username or passwprd!')
    # else:
    #     form = LoginForm()
        
    # context = {"form":form}
    return render(request, "users/login.html")

def signup(request):
    form = RegistrationForm()
    context = {"form":form}
    return render(request, "users/signup.html", context)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            messages.warning(request,"User already exists!")
            return redirect("users:signup")
        except:    
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.set_password(password)
            new_user.save()
            new_user_account = UserAccount()
            new_user_account.user = new_user
            new_user_account.save()
            return redirect("users:login")
            
    
    
# @login_required
# def home(request):
#     return render(request, "home.html")

@login_required
def profile(request):
    login_user = request.user.id
    account = UserAccount.objects.filter(user_id=login_user)
    posts = Post.objects.filter(user_id=login_user)
    context = {
        "account_details":account,
        "posts":posts,
    }
    return render(request, "users/profile.html", context)

def user_profile(request, user_id):
    user_account = UserAccount.objects.filter(user_id=user_id)
    posts = Post.objects.filter(user_id=user_id)
    context = {
        "account_details":user_account,
        "posts":posts,
    }
    return render(request, "users/user-profile.html", context)

def create(request):
    return render(request, "base.html")

def logout(request):
    logout_user(request)
    return redirect("users:login")
