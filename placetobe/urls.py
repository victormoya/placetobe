from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from pages.views import LandingView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^events/', include('events.urls', namespace="events")),
                       url(r'^profiles/', include('profiles.urls', namespace="profiles")),
                       url(r'^search/', include('search.urls', namespace="search")),
                       url(r'^comments/', include('comments.urls', namespace="comments")),

                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', LandingView.as_view(), name='landing')
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
