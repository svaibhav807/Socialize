from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/None/default.jpg')
    cover_pic = models.ImageField(upload_to='cover_pics/', default='cover_pics/None/cover_default.jpg')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    likes = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    likes_user=models.ManyToManyField(User,related_name="liked")

    def __str__(self):
        return str(self.content)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null = True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.author + '-' + self.author

class Follow(models.Model):
    to_follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    follower = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.to_follow) + '<-' + str(self.follower)

