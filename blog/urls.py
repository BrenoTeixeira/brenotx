from django.conf.urls import patterns, url

from .views import PostListView, PostDetailView, TagListView

urlpatterns = patterns('blog.views',
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagListView.as_view(), name='post-tags'),
)