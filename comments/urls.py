from django.conf.urls import url, patterns

from comments.views import VotePositiveView, VoteNegativeView


urlpatterns = patterns('',
    url(r'^vote_positive/(?P<comment_id>\w+)/$', VotePositiveView.as_view(), name='vote_positive'),
    url(r'^vote_negative/(?P<comment_id>\w+)/$', VoteNegativeView.as_view(), name='vote_negative'),
    )