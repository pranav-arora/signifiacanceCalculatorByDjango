from __future__ import unicode_literals

from django.db import models

# Create your models here.

class name(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class input(models.Model):
    visitorControl = models.IntegerField(default=0,)
    visitorVariation = models.IntegerField(default=0)
    conversionControl = models.IntegerField(default=0)
    conversionVariation = models.IntegerField(default=0)