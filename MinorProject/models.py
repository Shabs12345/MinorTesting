from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email_id = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email_id
