from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
def default_time():
    """set default timezone for migrations"""
    return timezone.now()
    
class Stocks(models.Model):
    name = models.CharField(max_length=250)
    open = models.FloatField()
    volume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False,default=default_time)

    class Meta:
        verbose_name_plural = 'Mes Stocks'
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return '{}'.format(self.name)