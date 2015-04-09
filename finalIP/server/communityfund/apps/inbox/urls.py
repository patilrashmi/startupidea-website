from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
   url(r'^send/?$', views.msg_send, name='msg_send'),
)


