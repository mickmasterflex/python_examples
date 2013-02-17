from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
    """
    Base model
    """
    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField('Address', max_length=50, null=True, blank=True)
    address2 = models.CharField('Address line 2', max_length=50,
        null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=10, null=True, blank=True)


