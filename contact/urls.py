from django.conf.urls import patterns, url

from .views import ContactView, ThanksView

urlpatterns = patterns('contact.views',
    url(r'^$', ContactView.as_view(), name='form-view'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
)
