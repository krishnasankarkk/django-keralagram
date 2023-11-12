from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    # path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register-user/', views.register, name='register-user'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.user_profile, name='user-profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow'),
    path('update-fullname/<str:fullname>/', views.update_fullname, name='update-fullname'),
    path('update-profilepic/', views.update_profilepic, name='update-profilepic'),
]
