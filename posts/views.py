from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,Http404
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
import cloudinary.uploader as uploader

from .models import Post
from notifications.models import Notification
from users.models import UserAccount

def create_post(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=request.user.id)
            userAccount = UserAccount.objects.get(user_id=request.user.id)
        except user.DoesNotExist:
            raise Http404("User doesnt exists!")
        post = Post()
        post.user = user
        if 'uploaded_image' in request.FILES and request.FILES['uploaded_image']:
            img_url = uploader.upload(request.FILES['uploaded_image'])
            print(img_url)
            post.post_img = img_url['secure_url']
        else:
            post.post_img = None
        post.caption = request.POST['caption'] if request.POST['caption'] else None
        post.like = 0
        post.save()
        notification = Notification()
        notification.type = 'p'
        notification.sender = userAccount
        notification.receiver = userAccount
        notification.content = f'{userAccount} posted new content!'
        notification.save()
        messages.success(request, "Successfully saved post :)")
        previous_url = request.META.get('HTTP_REFERER', None)
        return redirect(previous_url)
    
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        messages.success(request, "Successfully deleted post :)")
    except post.DoesNotExist:
       messages.warning(request, "Post doesn't exists !")
    
    
    # previous_url = request.META.get('HTTP_REFERER', None)

    return redirect('users:profile')