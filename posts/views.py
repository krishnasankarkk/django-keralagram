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
        if 'uploaded_image' in request.FILES and request.FILES['uploaded_image']:
            post.post_img = request.FILES['uploaded_image']
        else:
            post.post_img = None
        post.caption = request.POST['caption'] if request.POST['caption'] else None
        post.like = 0
        print(request.POST['caption'])
        post.save()
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