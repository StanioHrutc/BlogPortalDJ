from django.db import models

from datetime import datetime
# Create your models here.
class Story(models.Model):
    title            = models.CharField(max_length=30)
    story_text       = models.TextField()
    publication_date = models.DateTimeField(default=datetime.now, blank=False)
    story_photo      = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title