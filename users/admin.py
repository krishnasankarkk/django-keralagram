from django.contrib import admin
from .models import UserAccount

# Register your models here.
@admin.register(UserAccount)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
