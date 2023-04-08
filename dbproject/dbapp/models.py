from django.db import models

# Create your models here.

from django.db import models
class Artifact(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Level = models.IntegerField(null=True)
    Description = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.Name