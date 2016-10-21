from django.conf.urls import url
from django.contrib import admin
from blog.views import listPost
urlpatterns = [
    url(r'^$', listPost),
]
