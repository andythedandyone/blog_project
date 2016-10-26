from django.conf.urls import url
from django.contrib import admin
from blog.views import listPost, view_post


urlpatterns = [
    url(r'^$', listPost, name='home'),
    url(r'view_post/(?P<id>\d+)/$', view_post, name='view_post')
]
