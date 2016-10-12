from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Subreddit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        return Post.objects.filter(subreddit=self).count()

    def today_count(self):
        timespan = datetime.now() - timedelta(days=1)
        return Post.objects.filter(subreddit=self).filter(creation_time__gte=timespan).count()

    def daily_average(self):
        timespan = datetime.now() - timedelta(days=7)
        return round(Post.objects.filter(subreddit=self).filter(creation_time__gte=timespan).count()/7, 3)

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
        timespan = datetime.now() - timedelta(days=1)
        if Post.objects.filter(creation_time__gte=timespan):
            return True

    def is_hot(self):
        pass

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=255)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
