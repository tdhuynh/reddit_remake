from django.conf.urls import url
from django.contrib import admin
from reddit_app.views import SubredditView, SubredditDetailView, PostDetailView, \
                             SubredditCreateView, SubredditUpdateView, PostCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SubredditView.as_view(), name='subreddit_view'),
    url(r'^create/$', SubredditCreateView.as_view(), name='subreddit_create_view'),
    url(r'^(?P<pk>\d+)/$', SubredditDetailView.as_view(), name='subreddit_detail_view'),
    url(r'^(?P<pk>\d+)/update/$', SubredditUpdateView.as_view(), name='subreddit_update_view'),
    url(r'^post/$', PostCreateView.as_view(), name='post_create_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_view'),
]
