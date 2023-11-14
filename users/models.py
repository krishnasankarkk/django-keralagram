from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# from cloudinary.models import CloudinaryField

# Create your models here.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    profile_pic = models.ImageField(upload_to="uploads/",blank=True,null=True)
    # profile_pic = CloudinaryField('image')
    followers = ArrayField(models.IntegerField(blank=True),blank=True,null=True,default=list)
    following = ArrayField(models.IntegerField(blank=True),blank=True,null=True,default=list)
    posts = models.IntegerField(default=0)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.user.username
    