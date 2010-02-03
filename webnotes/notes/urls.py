from django.conf.urls.defaults import *

import views

urlpatterns = patterns('', 
    
    url(r'^list/$', views.notes_list, name='notes_list'),  
    url(r'^detail/(?P<id>\d+)/$', views.notes_detail, name='notes_detail'),  
    url(r'^new/$', views.notes_create, name='notes_create'),  
    url(r'^update/(?P<id>\d+)/$', views.notes_update, name='notes_update'),  
    url(r'^delete/(?P<id>\d+)/$', views.notes_delete, name='notes_delete'),  
)
