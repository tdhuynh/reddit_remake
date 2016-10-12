from django.db import models
from django.contrib.auth.models import User


class Subreddit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        pass

    def today_count(self):
        pass

    def daily_average(self):
        pass

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=175)
    description = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    def is_recent(self):
        pass

    def is_hot(self):
        pass
