from django.urls import path
from . import views

app_name = "messenger"
urlpatterns = [
    path('messages', views.messenger, name='home'),
    path('chat/<str:user_id>/', views.chat_user, name='chat'),
    path('sent-message/<int:user_id>', views.sent_message, name="sent-message"),
]