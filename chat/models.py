from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User,related_name='from_author_mssgs', on_delete=models.CASCADE)
    to = models.ForeignKey(User, related_name='to_author_mssgs', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    # def last_10_messages(self, user1, user2):
    #     return Message.objects.order_by('-timestamp').filter(author__in=[user1, user2]).all()[:10]
