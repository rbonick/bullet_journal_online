__author__ = 'rbonick'

from django.conf.urls import patterns, url
from entries import views


urlpatterns = patterns('',
    # Web pages
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', views.view_month_entries, name="entries"),
    url(r'^next-seven/$', views.view_next_seven_days_entries, name="home"),
    url(r'^archive/$', views.view_archive, name="view_archive"),

    # Form urls
    url(r'^create/$', views.create_entry, name="create_entry"),

    # Ajax urls
    url(r'^toggle-todo/(?P<todo_id>\d+)/$', views.toggle_todo, name="toggle_todo"),
)