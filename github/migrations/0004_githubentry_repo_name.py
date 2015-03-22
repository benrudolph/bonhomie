# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0003_githubentry_github_avatar_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubentry',
            name='repo_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
