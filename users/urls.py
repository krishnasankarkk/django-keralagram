from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='create-user'),
    path('profile', views.profile, name='profile'),
    path('user-create', views.create, name='create-user'),
]
