from django.conf.urls import url, include
from django.contrib import admin
from reddit_app.views import SubredditView, SubredditDetailView, PostDetailView, \
                             SubredditCreateView, SubredditUpdateView, PostCreateView, \
                             UserCreateView, PostUpdateView, CommentCreateView, CommentUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', SubredditView.as_view(), name='subreddit_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^create_sub/$', SubredditCreateView.as_view(), name='subreddit_create_view'),
    url(r'^(?P<pk>\d+)/$', SubredditDetailView.as_view(), name='subreddit_detail_view'),
    url(r'^(?P<pk>\d+)/update_sub/$', SubredditUpdateView.as_view(), name='subreddit_update_view'),
    url(r'^(?P<pk>\d+)/create_post/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^(?P<pk>\d+)/post/$', PostDetailView.as_view(), name='post_detail_view'),
    url(r'^(?P<pk>\d+)/post/update_post/$', PostUpdateView.as_view(), name='post_update_view'),
    url(r'^post/(?P<pk>\d+)/create_comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^(?P<pk>\d+)/update_comment/$', CommentUpdateView.as_view(), name='comment_update_view'),
]
