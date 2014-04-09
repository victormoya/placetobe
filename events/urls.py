from django.conf.urls import patterns, url
from comments.views import SortByLikesView, PostCommentView
from events.views import EventList, PublishEventView, EventDetailView, AddAssistantView, RemoveAssistantView, \
    EventSuggestedView


urlpatterns = patterns('',
    url(r'^$', EventList.as_view(), name='list'),
    url(r'^suggested/$', EventSuggestedView.as_view(), name='suggested'),
    url(r'^add/$', PublishEventView.as_view(), name='add'),
    url(r'^assist/(?P<event_id>\w+)/$', AddAssistantView.as_view(), name='assist'),
    url(r'^not_assist/(?P<event_id>\w+)/$', RemoveAssistantView.as_view(), name='not_assist'),
    url(r'^detail/(?P<event_id>\w+)/$', EventDetailView.as_view(), name='detail'),
    url(r'^detail/(?P<event_id>\w+)/comments/$', PostCommentView.as_view(), name='post_comment'),
    url(r'^detail/(?P<event_id>\w+)/comments/(?P<comment_id>\w+)/$', PostCommentView.as_view(), name='post_reply'),
    url(r'^detail/(?P<event_id>\w+)/comments/sorted$', SortByLikesView.as_view(), name='sort_likes'),
)