import json
import requests
import time
from datetime import datetime, timedelta
from pytz import utc

from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from restless.modelviews import ListEndpoint
from restless.views import Endpoint

from .models import GithubEntry

FMT = '%Y-%m-%dT%H:%M:%SZ'
JSONSerializer = serializers.get_serializer("json")


class GithubMarkdown(View):

    def get(self, request, entry_id):
        entry = GithubEntry.objects.get(pk=entry_id)
        data = {
            'text': entry.body,
            'mode': 'gfm' if entry.repo_name else 'markdown',
            'context': entry.repo_name,
        }

        resp = requests.post('https://api.github.com/markdown', data=json.dumps(data))

        return HttpResponse(resp)


class GithubWebhook(View):

    def post(self, request):

        data = json.loads(request.body)

        action = data.get('action')
        pull_request = data.get('pull_request')

        if action == 'closed' and pull_request and pull_request.get('merged_at'):
            title = pull_request.get('title')
            tag = None

            for t, color in settings.BONHOMIE_TAGS:
                formatted_tag = u"#{tag}".format(tag=t)
                if formatted_tag in title:
                    tag = t
                    title = title.replace(formatted_tag, '').strip()
                    break

            if tag:
                merged_at = datetime.strptime(pull_request.get('merged_at'), FMT)
                merged_at = merged_at.replace(tzinfo=utc)

                entry = GithubEntry(
                    title=title,
                    body=pull_request.get('body'),
                    repo_name=pull_request.get('base').get('repo').get('full_name'),
                    tag=tag,
                    url=pull_request.get('html_url'),
                    merged_at=merged_at,
                    merge_commit_sha=pull_request.get('merge_commit_sha'),
                    github_username=pull_request.get('user').get('login'),
                    github_avatar_url=pull_request.get('user').get('avatar_url'),

                )
                entry.save()

        return HttpResponse('', 'application/json')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(GithubWebhook, self).dispatch(*args, **kwargs)

class GithubEntryList(ListEndpoint):
    model = GithubEntry

    def get_query_set(self, request, *args, **kwargs):
        qs = super(GithubEntryList, self).get_query_set(request, *args, **kwargs)

        day_start = int(request.GET.get('day_start', 0))
        day_end = int(request.GET.get('day_end', 0))

        qs = qs.filter(
                merged_at__lte=timezone.now() - timedelta(days=day_start)
            ).filter(
                merged_at__gt=timezone.now() - timedelta(days=day_end)
            ).order_by('-merged_at').values(
                'id', 'title', 'tag', 'merged_at', 'url', 'repo_name', 'github_username', 'github_avatar_url'
            )
        return qs
