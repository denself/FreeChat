from django.conf.urls import patterns, url
from views import default, signIn, signOut

urlpatterns = patterns('',
    url(r'^$', default),
    url(r'^signin/$', signIn),
    url(r'^signout', signOut)
)