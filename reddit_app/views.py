from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from reddit_app.models import Subreddit, Post, Comment, PostVote, CommentVote

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

    def get_queryset(self):
        return Subreddit.objects.filter(user=self.request.user)


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

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

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
        post_id = Comment.objects.get(id=self.kwargs["pk"]).post.id
        return reverse('post_detail_view', args=[post_id])

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class PostVoteView(CreateView):
    model = PostVote
    success_url = '/'
    fields = ('value',)

    def form_valid(self, form):
        try:
            PostVote.objects.get(user=self.request.user, post_id=self.kwargs['pk']).delete()
        except PostVote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class CommentVoteView(CreateView):
    model = CommentVote
    fields = ('value',)

    def get_success_url(self, **kwargs):
        post_id = Comment.objects.get(id=self.kwargs['pk']).post.id
        return reverse('post_detail_view', args=[post_id])

    def form_valid(self, form):
        try:
            CommentVote.objects.get(user=self.request.user, comment_id=self.kwargs['pk']).delete()
        except CommentVote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment = Comment.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
