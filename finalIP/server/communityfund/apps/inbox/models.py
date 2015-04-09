from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="messages_sent")
    receiver = models.ForeignKey(User, related_name="messages_recieved")
    title = models.TextField(max_length=1024)
    content = models.TextField(max_length=20480)

