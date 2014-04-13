from django.conf.urls import patterns, url

from .views import PostListView, PostDetailView

urlpatterns = patterns('blog.views',
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post-detail'),
)
