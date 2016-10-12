from django.contrib import admin
from reddit_app.models import Subreddit, Post, Comment

admin.site.register([Subreddit, Post, Comment])
