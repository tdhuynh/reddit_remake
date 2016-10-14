from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from reddit_app.models import Subreddit, Post, Comment

from django.urls import reverse_lazy


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


class SubredditCreateView(CreateView):
    model = Subreddit
    success_url = "/"
    fields = ('name', 'description',)


class SubredditUpdateView(UpdateView):
    model = Subreddit
    success_url = "/"
    fields = ('name', 'description',)


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('subreddit_detail_view')
    fields = ('title', 'description', 'url')
