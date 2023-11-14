from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('create-post', views.create_post, name='create-post'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete-post'),
]
