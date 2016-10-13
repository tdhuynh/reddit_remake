from django.conf.urls import url
from django.contrib import admin
from reddit_app.views import index_view, SubredditView, SubredditDetailView, PostDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index_view'),
    url(r'^subreddits/$', SubredditView.as_view(), name='subreddit_view'),
    url(r'^subreddits/(?P<pk>\d+)/$', SubredditDetailView.as_view(), name='subreddit_detail_view'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_view'),
]
