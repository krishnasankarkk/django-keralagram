from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Q


from users.models import UserAccount 
from .models import Message 

# Create your views here.
def chat_user(request, user_id):
    user = UserAccount.objects.get(user_id=user_id)
    messages = Message.objects.filter(Q(from_user=request.user.id) & Q(to_user=user_id) | Q(from_user=user_id) & Q(to_user=request.user.id)).order_by('created_at')

    context = {
        "chat_user": user,
        "all_messages": messages,
    }
    return render(request, "messenger/chat.html", context)

def sent_message(request, user_id):
    if request.method == 'POST':
        message = request.POST.get('message-input')
        from_user = User.objects.get(id=request.user.id)
        to_user = User.objects.get(id=user_id)
        new_message = Message()
        new_message.from_user = from_user
        new_message.to_user = to_user
        new_message.message = message
        new_message.save()
        previous_url = request.META.get('HTTP_REFERER', None)
        return HttpResponseRedirect(previous_url)
