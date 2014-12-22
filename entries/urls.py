__author__ = 'rbonick'

from django.conf.urls import patterns, url
from entries import views


urlpatterns = patterns('',
    url(r'^$', views.view_all_entries, name="entries"),
)