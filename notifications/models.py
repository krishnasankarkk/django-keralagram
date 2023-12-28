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
    sender = models.IntegerField(default=None, null=True, blank=True)
    receiver = models.IntegerField(default=None, null=True, blank=True)
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)