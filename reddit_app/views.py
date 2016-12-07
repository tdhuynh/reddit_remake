from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from reddit_app.models import Subreddit, Post, Comment

from django.urls import reverse

class IndexView(ListView):
    template_name = 'index.html'
    model = Post


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
    fields = ('name', 'description',)

    def get_success_url(self, **kwargs):
        return reverse('subreddit_detail_view', args=[int(self.kwargs['pk'])])


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'url')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('subreddit_detail_view', args=[int(self.kwargs['pk'])])


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'description', 'url')

    def get_success_url(self, **kwargs):
        return reverse('post_detail_view', args=[int(self.kwargs['pk'])])


class CommentCreateView(CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('post_detail_view', args=[int(self.kwargs['pk'])])


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('text',)

    def get_success_url(self, **kwargs):
        return reverse('post_detail_view', args=[int(self.kwargs['pk'])])


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
