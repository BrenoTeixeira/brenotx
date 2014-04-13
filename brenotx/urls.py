from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Apps urls
    url(r'^$', RedirectView.as_view(pattern_name='blog:post-list'), name='go-to-blog'),

    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^contact/', include('contact.urls', namespace="contact")),

    # Third-party urls
    (r'^ckeditor/', include('ckeditor.urls')),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
)
