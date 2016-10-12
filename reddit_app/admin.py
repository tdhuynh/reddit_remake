from django.contrib import admin
from reddit_app.models import Subreddit, Post

admin.site.register([Subreddit, Post])
