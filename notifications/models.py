from django.db import models

from users.models import UserAccount

class Notification(models.Model):
    """
        Model to store user generated notifications like message recieved.
    """
    notification_types = [
        ('m', 'Message'),
        ('p', 'Post'),
        ('l', 'Like'),
        ('c', 'Comment'),
    ]
    type = models.CharField(choices=notification_types, default=None)
    sender = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="receiver")
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    