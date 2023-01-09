from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Tweet(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    alreadyLiked = models.BooleanField(default=False)
    alreadyDisliked = models.BooleanField(default=False)
    previous_users = ArrayField(models.IntegerField(), default=list)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    alreadyLiked = models.BooleanField(default=False)
    alreadyDisliked = models.BooleanField(default=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    previous_users = ArrayField(models.IntegerField(), default=list)

    def __str__(self):
        return self.user.username


