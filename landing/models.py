from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stocks(models.Model):
    name = models.CharField(max_length=250)
    open = models.FloatField()
    volume = models.IntegerField()
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return '{}'.format(self.name)