from os.path import abspath, dirname, join
import json

from django.test import TestCase, Client
from django.utils import timezone
from django.core.urlresolvers  import reverse
from datetime import timedelta

from github.models import GithubEntry


THISDIR = dirname(abspath(__file__))
BASE_PATH = join(THISDIR, 'data')
SAMPLE_RESP = 'sample_response.json'

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_payload(self):
        data = open(join(BASE_PATH, SAMPLE_RESP), 'r').read()

        self.client.post(reverse('payload'), content_type='application/json', data=data)

        entry = GithubEntry.objects.first()
        self.assertEqual(entry.tag, 'bug')
        self.assertEqual(entry.title, 'Update README.md')
        self.assertEqual(entry.repo_name, 'benrudolph/numeric_converter')

    def test_list(self):
        data = {
            'title': 'a',
            'body': 'b',
            'merge_commit_sha': 'c',
            'merged_at': timezone.now(),
            'url': 'd',
            'repo_name': 'e',
            'github_username': 'f',
            'github_avatar_url': 'g',
        }
        e1 = GithubEntry(**data)
        e1.save()

        data['merged_at'] = timezone.now() - timedelta(days=3)
        e2 = GithubEntry(**data)
        e2.save()

        resp = self.client.get(reverse('entries'), data={'day_start': 0, 'day_end': 2})

        content = json.loads(resp.content)
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]['id'], e1.id)

