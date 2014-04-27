from django.conf.urls import patterns, url
from views import default

urlpatterns = patterns('',
    url(r'^$', default),
)