from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,Http404
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages


from .models import Post

def create_post(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=request.user.id)
        except user.DoesNotExist:
            raise Http404("User doesnt exists!")
        post = Post()
        post.user = user
        # post.post_img = request.FILES['uploaded_image']
        post.caption = request.POST['caption']
        post.like = 0
        post.save()
        # previous_url = request.META.get('HTTP_REFERER', None)

        return redirect('users:profile')
    
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        messages.success(request, "Successfully deleted post :)")
    except post.DoesNotExist:
       messages.warning(request, "Post doesn't exists !")
    
    
    # previous_url = request.META.get('HTTP_REFERER', None)

    return redirect('users:profile')