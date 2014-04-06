from django.conf.urls import patterns, url

from .views import PostListView

urlpatterns = patterns('blog.views',
    url(r'^$', PostListView.as_view(), name='post-list'),
)
