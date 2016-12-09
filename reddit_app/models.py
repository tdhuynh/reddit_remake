from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Subreddit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        return self.post_set.count()

    def today_count(self):
        timespan = datetime.now() - timedelta(days=1)
        return self.post_set.filter(creation_time__gte=timespan).count()

    def daily_average(self):
        timespan = datetime.now() - timedelta(days=7)
        return round(self.post_set.filter(creation_time__gte=timespan).count()/7, 3)

    def recent_posts(self):
        # return self.post_set.all()[:20]
        return self.post_set.all()

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

    class Meta:
        ordering = ("-creation_time",)

    def is_recent(self):
        timespan = datetime.now() - timedelta(days=1)
        if Post.objects.filter(creation_time__gte=timespan):
            return "YES"
        else:
            return "NO"

    def is_hot(self):
        timespan = datetime.now() - timedelta(hours=3)
        if self.comment_set.filter(created_time__gt=timespan).count() > 3:
            return "YES"
        else:
            return "NO"

    def all_comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

    @property
    def score(self):
        return sum([post_obj.score for post_obj in self.postvote_set.all()])


class Comment(models.Model):
    text = models.TextField(max_length=255)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def score(self):
        return sum([comment_obj.comment_score for comment_obj in self.commentvote_set.all()])

class PostVote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    value = models.BooleanField()

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return "{} - {}".format(self.post.title, self.score)

    @property
    def score(self):
        if self.value:
            return 1
        return -1


class CommentVote(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    value = models.BooleanField()

    class Meta:
        unique_together = ('user', 'comment')

    @property
    def comment_score(self):
        if self.value:
            return 1
        return -1
