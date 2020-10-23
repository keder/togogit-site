import datetime

from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True)


class Note(models.Model):
    text = models.CharField(max_length=1000, null=False)
    repo = models.CharField(max_length=200, null=True)
    file_path = models.CharField(max_length=200, null=True)
    line = models.SmallIntegerField(null=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class UserNote(models.Model):
    text = models.CharField(max_length=1000, null=False)
    creation_time = models.CharField(max_length=64, null=True, default=datetime.date.today)
