"""
URL configuration for instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home, login

urlpatterns = [
    # path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('user/', include('users.urls'), name="users"),
    path('posts/', include('posts.urls'), name="posts"),
    path('messenger/', include('messenger.urls'), name="messenger"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)