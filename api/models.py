from django.db import models

# Create your models here.
class PAModel(models.Model):
    Date = models.DateTimeField()
    Last = models.FloatField()
    Volume = models.IntegerField()