import datetime

from django.db import models


class UserNote(models.Model):
    text = models.CharField(max_length=1000, null=False)
    creation_time = models.CharField(max_length=64, null=True, default=datetime.date.today)

