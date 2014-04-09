from django.conf.urls import patterns, url

from profiles.views import RegistrationView, LoginView, LogoutView, EditView, DetailView

urlpatterns = patterns('',
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^edit/(?P<pk>\w+)/$', EditView.as_view(), name='edit'),
    url(r'^detail/(?P<publisher>\w+)/$', DetailView.as_view(), name='detail'),
)