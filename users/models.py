from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(upload_to="uploads/",null=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.user.username
