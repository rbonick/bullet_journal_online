from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from bullet_journal_online.views import index

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
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
