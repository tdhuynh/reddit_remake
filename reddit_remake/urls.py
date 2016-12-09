from django.conf.urls import url, include
from django.contrib import admin
from reddit_app.views import SubredditView, SubredditDetailView, PostDetailView, \
                             SubredditCreateView, SubredditUpdateView, PostCreateView, \
                             UserCreateView, PostUpdateView, CommentCreateView, CommentUpdateView, \
                             IndexView, PostVoteView, CommentVoteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^subreddits/$', SubredditView.as_view(), name='subreddit_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^create_sub/$', SubredditCreateView.as_view(), name='subreddit_create_view'),
    url(r'^(?P<pk>\d+)/$', SubredditDetailView.as_view(), name='subreddit_detail_view'),
    url(r'^(?P<pk>\d+)/update_sub/$', SubredditUpdateView.as_view(), name='subreddit_update_view'),
    url(r'^(?P<pk>\d+)/create_post/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_view'),
    url(r'^post/(?P<pk>\d+)/update_post/$', PostUpdateView.as_view(), name='post_update_view'),
    url(r'^post/(?P<pk>\d+)/create_comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^comment/(?P<pk>\d+)/update_comment/$', CommentUpdateView.as_view(), name='comment_update_view'),
    url(r'^post/(?P<pk>\d+)/upvote/$', PostVoteView.as_view(), name='post_upvote_view'),
    url(r'^post/(?P<pk>\d+)/downvote/$', PostVoteView.as_view(), name='post_downvote_view'),
    url(r'^comment/(?P<pk>\d+)/upvote/$', CommentVoteView.as_view(), name='comment_upvote_view'),
    url(r'^comment/(?P<pk>\d+)/downvote/$', CommentVoteView.as_view(), name='comment_downvote_view')
]
