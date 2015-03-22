from django.conf.urls import patterns, url

from .views import GithubWebhook, GithubEntryList, GithubMarkdown

urlpatterns = patterns('',
    url(r'^payload$', GithubWebhook.as_view(), name='payload'),
    url(r'^entries/$', GithubEntryList.as_view(), name='entries'),
    url(r'^markdown/(\d+)$', GithubMarkdown.as_view(), name='markdown'),
)
