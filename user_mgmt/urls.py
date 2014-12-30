__author__ = 'rbonick'

from django.conf.urls import patterns, url
from user_mgmt import views


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout_success.html'}),
    url(r'^register/$', views.register, name="register"),
)