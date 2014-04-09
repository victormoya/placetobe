from django.conf.urls import patterns, url

from search.views import SearchResultView

urlpatterns = patterns('',
    url(r'^$', SearchResultView.as_view(), name='result'),

    )