from datetime import timedelta

from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.utils import timezone

from github.models import GithubEntry

class BonhomieView(TemplateView):
    template_name = 'ui/index.html'

    def get(self, request):
        entries = GithubEntry.objects.filter(
            merged_at__gt=timezone.now() - timedelta(days=7)
        ).order_by(
            '-merged_at'
        )


        context = {
            'tags': settings.BONHOMIE_TAGS,
            'title': settings.BONHOMIE_TITLE,
            'description': settings.BONHOMIE_DESCRIPTION,
        }
        return render(request, self.template_name, context)


