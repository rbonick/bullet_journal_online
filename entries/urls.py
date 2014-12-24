__author__ = 'rbonick'

from django.conf.urls import patterns, url
from entries import views


urlpatterns = patterns('',
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', views.view_month_entries, name="entries"),
    url(r'^$', views.view_month_entries, name="home"),
)