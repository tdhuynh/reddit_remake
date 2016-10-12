from django.shortcuts import render

from reddit_app.models import Subreddit, Post, Comment


def index_view(request):
    context = {
        "all_subreddit": Subreddit.objects.all(),
        "all_post": Post.objects.all(),
        "all_comments": Comment.objects.all(),
    }
    return render(request, 'index.html', context)
