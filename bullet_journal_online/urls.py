from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ArchiveIndexView

from bullet_journal_online.views import index
from entries.models import Task

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bullet_journal_online.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Admin page
    url(r'^admin/', include(admin.site.urls)),

    # Index page
    url(r'^$', index, name="index"),

    # Entries
    url(r'^entry/', include('entries.urls')),

    # Archive

    # User management
    url(r'^user/', include('user_mgmt.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
