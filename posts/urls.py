from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('create-post', views.create_post, name='create-post'),
    # path('save-post', views.save_post, name='save-post'),
]
