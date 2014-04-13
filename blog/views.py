from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published=True)

