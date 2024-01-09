from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime 
from django.db.models import F, ExpressionWrapper, DurationField

from users.models import UserAccount
from posts.models import Post

@login_required(login_url='/user/login')
def home(request):
    users = UserAccount.objects.exclude(user_id=request.user.id).order_by('-created_at')
    user = UserAccount.objects.get(user_id=request.user.id)
    following = user.following
    following_posts = Post.objects.filter(user__id__in=following).order_by('-created_at')
    current_date = datetime.datetime.now(datetime.timezone.utc)
    posts = Post.objects.all().order_by('-created_at').annotate(
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
        "current_user": user,
        "users":users,
        "all_posts":updated_posts,
        "following_posts":following_posts,
        "location":"home",
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
