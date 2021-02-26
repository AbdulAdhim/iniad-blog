from django.db import models
from django.contrib.auth import get_user_model
# from django.urls import reverse

User = get_user_model()

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # room = models.CharField(max_length=50, default='room')

    def __str__(self):
        return self.author.username

    def last_20_messages():
        return Message.objects.order_by('-timestamp').all()[:20]
