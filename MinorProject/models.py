from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Users(models.Model):
    comp_id = models.CharField(max_length=100,blank=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email_id = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def save(self, *args, **kwargs):
        obj = Users.objects.last()
        if obj is None:
            self.comp_id = "MPR0001"
        else:
            c_id = obj.comp_id
            c_id = int(c_id[3:]) + 1
            self.comp_id = "MPR%04d" % c_id
        super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return self.email_id
