from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'author', 'tags', 'published')
    list_display = ['title', 'created_at', 'updated_at', 'published']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'updated_at', 'author']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)