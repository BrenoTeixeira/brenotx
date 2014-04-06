from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(editable=False)
    content = models.TextField()
    author = models.ForeignKey('auth.User')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
