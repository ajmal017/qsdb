from django.db import models

# Create your models here.
class IBPricesModel(models.Model):
    symbol = models.CharField(max_length=7)
    date = models.DateTimeField()
    last = models.DecimalField(decimal_places=6,max_digits=11)
    volume = models.IntegerField()