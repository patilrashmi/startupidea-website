from django.conf.urls import patterns, url
from communityfund.apps.home import views


urlpatterns = patterns('',
   url(r'^/?$', views.index, name='index'),
   url(r'^user/(?P<pk>\d+)/?$', views.user_details, name='user'),

   url(r'^ideas/?$', views.ideas, name='ideas'),
   url(r'^idea/create/?$', views.IdeaCreate.as_view(), name='idea_create'),
   url(r'^idea/(?P<pk>\d+)/?$', views.idea_details, name='idea'),
   url(r'^idea/(?P<pk>\d+)/edit/?$', views.IdeaUpdate.as_view(), name='idea_update'),
   url(r'^idea/(?P<pk>\d+)/delete/?$', views.IdeaDelete.as_view(), name='idea_delete'),

   url(r'^categories/?$', views.categories, name='categories'),
   url(r'^category/create/?$', views.create_category, name="create_category"),
   url(r'^category/(?P<pk>\d+)/?$', views.category_details, name='category'),
   url(r'^category/(?P<pk>\d+)/subscribe/?$', views.category_subscribe, name='subscribe'),
   url(r'^category/(?P<pk>\d+)/unsubscribe/?$', views.category_unsubscribe, name='unsubscribe'),

)


