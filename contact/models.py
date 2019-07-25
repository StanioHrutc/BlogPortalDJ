from django.db import models

# Create your models here.


class Contact(models.Model):
    name          = models.CharField(max_length=20)
    sur_name      = models.CharField(max_length=20)
    email         = models.EmailField(max_length=70)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.name