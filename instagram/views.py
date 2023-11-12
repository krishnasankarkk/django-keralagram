from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user
from users.models import UserAccount
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect

@login_required(login_url='/user/login')
def home(request):
    users = UserAccount.objects.exclude(user_id=request.user.id)
    context = {
        "users":users,
    }
    return render(request, "home.html", context)

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=user_name)
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login_user(request, user)
                messages.success(request, "Login successfull :)")
                return redirect("home")
            else:
                messages.warning(request, "Wrong password!")
                return render(request, "users/login.html", {'success':False})
        except:
            messages.warning(request, "Invalid username!")
            return render(request, "users/login.html", {'success':False})
