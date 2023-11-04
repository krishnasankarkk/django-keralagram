from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserAccount

@login_required
def home(request):
    users = UserAccount.objects.exclude(user_id=request.user.id)
    context = {
        "users":users,
    }
    return render(request, "home.html", context)