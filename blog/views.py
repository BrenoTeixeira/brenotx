from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Post


class PostListView(ListView):
    model = Post

