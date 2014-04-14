from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published=True)

