from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post

from taggit.models import Tag


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostListView(TagMixin, ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published=True)


class TagListView(TagMixin, ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))




