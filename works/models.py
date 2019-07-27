from django.db import models

from datetime import datetime
# Create your models here.


class Work(models.Model):

    title         = models.CharField(max_length=30, blank=False)
    description   = models.CharField(max_length=90, blank=False)
    link          = models.CharField(max_length=200, blank=False)
    img           = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    creation_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title