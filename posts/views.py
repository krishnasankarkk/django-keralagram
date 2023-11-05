from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,Http404
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth.models import User
from django.urls import reverse


from .models import Post

def create_post(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=request.user.id)
        except user.DoesNotExist:
            raise Http404("User doesnt exists!")
        post = Post()
        post.user = user
        post.post_img = request.FILES['uploaded_image']
        post.like = 0
        post.save()
        previous_url = request.META.get('HTTP_REFERER', None)

        return HttpResponseRedirect(previous_url)