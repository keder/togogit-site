from django.db import models

# Create your models here.


class Note(models.Model):
    text = models.CharField(null=False)
    repo = models.CharField(null=True)
    file_path = models.CharField(null=True)
    line = models.SmallIntegerField(null=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    
class Repository(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(null=True)
