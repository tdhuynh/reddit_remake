from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from reddit_app.models import Subreddit, Post, Comment


def index_view(request):
    context = {
        "all_subreddit": Subreddit.objects.all(),
        "all_post": Post.objects.all(),
        "all_comments": Comment.objects.all(),
    }
    return render(request, 'index.html', context)


class SubredditView(ListView):
    template_name = 'subreddits.html'
    model = Subreddit


class SubredditDetailView(DetailView):
    model = Subreddit


class PostDetailView(DetailView):
    model = Post
