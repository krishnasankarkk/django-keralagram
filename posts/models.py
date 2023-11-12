from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to="uploads/", null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        name = str(self.user)+"_"+str(self.id) 
        return name