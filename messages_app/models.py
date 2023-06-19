import uuid
from django.db import models
from django.contrib.auth.models import User
"""
Model for 'messages_app'
"""
class Message(models.Model):
    sender = models.ForeignKey(
        'profiles.Profile',
        related_name="sender",
        on_delete=models.CASCADE
    )

    reciever = models.ForeignKey(
        'profiles.Profile',
        related_name="reciever",
        on_delete=models.CASCADE
    )

    msg_content = models.TextField()

    created_at = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    user_one = models.ForeignKey(
        'profiles.Profile',
        related_name='user_one',
        on_delete=models.CASCADE
    )

    user_two = models.ForeignKey(
        'profiles.Profile',
        related_name='user_two',
        on_delete=models.CASCADE
    )

    messages = models.ManyToManyField(Message, related_name='messages', blank=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
