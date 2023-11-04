from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    # path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='create-user'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.user_profile, name='user-profile'),
    # path('user-create', views.create, name='create-user'),
]
