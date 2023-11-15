from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    from_user = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="recieve_messages", on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"From: {self.from_user}, To: {self.to_user}"
