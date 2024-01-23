from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib import messages
from django.db.models import Q, F, ExpressionWrapper, DurationField
import datetime 

from .forms import LoginForm, RegistrationForm
from .models import UserAccount
from posts.models import Post

def login_view(request):
    return render(request, "users/login.html")

def signup(request):
    form = RegistrationForm()
    context = {
        "form":form,
        "gender_choices":{
            "M": "Male",
            "F": "Female",
            "O": "Other",
        }
    }
    return render(request, "users/signup.html", context)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        try:
            user = User.objects.get(Q(username=username))
            print(user)
            messages.warning(request,"User already exists!")
            return redirect("users:signup")
        except:    
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.first_name = fullname.split()[0]
            new_user.last_name = fullname.split()[1]
            new_user.set_password(password)
            new_user.save()
            new_user_account = UserAccount()
            new_user_account.user = new_user
            new_user_account.full_name = fullname
            new_user_account.phone = phone
            new_user_account.gender = gender
            new_user_account.save()
            messages.success(request,"User created successfully :)")
            return redirect("users:login")
            
    
    
# @login_required
# def home(request):
#     return render(request, "home.html")

@login_required(login_url='/user/login')
def profile(request):
    account = UserAccount.objects.get(user_id=request.user.id)
    followers = len(account.followers) if account.followers is not None else 0
    following = len(account.following) if account.following is not None else 0
    current_date = datetime.datetime.now(datetime.timezone.utc)
    posts = Post.objects.filter(user_id=request.user.id).order_by('-created_at').annotate(
        time_difference = ExpressionWrapper(current_date - F('created_at'), output_field=DurationField())
    )
    updated_posts = []
    for post in posts:
        time_difference = post.time_difference
        days = time_difference.days
        hours = time_difference.seconds // 3600
        minutes = (time_difference.seconds // 60) % 60
        
        if days > 0:
            updated_time_difference = f"{days} day{'s' if days != 1 else ''}"
        elif hours > 0:
            updated_time_difference = f"{hours} hour{'s' if hours != 1 else ''}"
        elif minutes > 0:
            updated_time_difference = f"{minutes} minute{'s' if minutes != 1 else ''}"
        else:
            updated_time_difference = "Few seconds"
        updated_post = {
            'id' : post.id,
            'post_img' : post.post_img,
            'like' : post.like,
            'user' : post.user,
            'caption' : post.caption,
            'time_difference' : updated_time_difference,
        }
        updated_posts.append(updated_post)
    context = {
        "current_user":account,
        "posts":updated_posts,
        "posts_count":posts.count(),
        "followers":followers,
        "following":following,
        "location":"profile",
    }
    return render(request, "users/profile.html", context)

def user_profile(request, user_id):
    user_account = UserAccount.objects.get(user_id=user_id)
    account = UserAccount.objects.get(user_id=request.user.id)
    followers = len(user_account.followers) if user_account.followers is not None else 0
    following = len(user_account.following) if user_account.following is not None else 0
    if user_account.followers is not None and request.user.id in user_account.followers: 
        followed = True
    else:
        followed = False
    current_date = datetime.datetime.now(datetime.timezone.utc)
    posts = Post.objects.filter(user_id=user_id).order_by('-created_at').annotate(
        time_difference = ExpressionWrapper(current_date - F('created_at'), output_field=DurationField())
    )
    updated_posts = []
    for post in posts:
        time_difference = post.time_difference
        days = time_difference.days
        hours = time_difference.seconds // 3600
        minutes = (time_difference.seconds // 60) % 60
        
        if days > 0:
            updated_time_difference = f"{days} day{'s' if days != 1 else ''}"
        elif hours > 0:
            updated_time_difference = f"{hours} hour{'s' if hours != 1 else ''}"
        elif minutes > 0:
            updated_time_difference = f"{minutes} minute{'s' if minutes != 1 else ''}"
        else:
            updated_time_difference = "Few seconds"
        updated_post = {
            'id' : post.id,
            'post_img' : post.post_img,
            'like' : post.like,
            'user' : post.user,
            'caption' : post.caption,
            'time_difference' : updated_time_difference,
        }
        updated_posts.append(updated_post)
    context = {
        "current_user":account,
        "account_details":user_account,
        "posts":updated_posts,
        "posts_count":posts.count(),
        "followed":followed,
        "followers":followers,
        "following":following,
    }
    return render(request, "users/user-profile.html", context)

def logout(request):
    logout_user(request)
    messages.success(request, "Logout successfull :)")
    return redirect("users:login")

@login_required(login_url='/user/login')
def follow_user(request, user_id):
    user_to_follow = UserAccount.objects.get(user_id=user_id)
    current_user = UserAccount.objects.get(user_id=request.user.id)
    if user_to_follow.followers is not None and current_user.user_id in user_to_follow.followers:
        return JsonResponse({'status': 'fail'}) 
    else:
        user_to_follow.followers.append(current_user.user_id)
        user_to_follow.save()
        current_user.following.append(user_to_follow.user_id)
        current_user.save()
        previous_url = request.META.get('HTTP_REFERER', None)
        return HttpResponseRedirect(previous_url)

@login_required(login_url='/user/login')
def unfollow_user(request, user_id):
    user_to_unfollow = UserAccount.objects.get(user_id=user_id)
    current_user = UserAccount.objects.get(user_id=request.user.id)
    if user_to_unfollow.followers is not None and current_user.user_id in user_to_unfollow.followers:
        user_to_unfollow.followers.remove(current_user.user_id)
        user_to_unfollow.save()
        current_user.following.remove(user_to_unfollow.user_id)
        current_user.save()
        previous_url = request.META.get('HTTP_REFERER', None)
        return HttpResponseRedirect(previous_url)
    else:
        return JsonResponse({'status': 'fail'}) 

def update_fullname(request):
    if request.method == 'POST':
        user = UserAccount.objects.get(user_id=request.user.id)
        user.full_name = request.POST.get('fullname')
        user.save()
        previous_url = request.META.get('HTTP_REFERER', None)
        return HttpResponseRedirect(previous_url)
    else:
        raise Http404("Failed to update Full name !") 
    
def update_profilepic(request):
    if request.method == 'POST':
        user = UserAccount.objects.get(user_id=request.user.id)
        user.profile_pic = request.FILES['uploaded_profile_pic']
        user.save()
        previous_url = request.META.get('HTTP_REFERER', None)
        return HttpResponseRedirect(previous_url)
    else:
        raise Http404("Failed to update profile !") 
