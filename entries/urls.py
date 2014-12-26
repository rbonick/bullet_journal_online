__author__ = 'rbonick'

from django.conf.urls import patterns, url
from entries import views


urlpatterns = patterns('',
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', views.view_month_entries, name="entries"),
    url(r'^next-seven/$', views.view_next_seven_days_entries, name="home"),
    url(r'^create/$', views.create_entry, name="create_entry"),
)