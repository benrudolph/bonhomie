from django.db import models

class GithubEntry(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    body = models.TextField(null=True)
    merged_at = models.DateTimeField()
    merge_commit_sha = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    repo_name = models.CharField(max_length=255, default='')

    # Github User info, eventually could be its own model
    github_username = models.CharField(max_length=255)
    github_avatar_url = models.CharField(max_length=255, default='')
