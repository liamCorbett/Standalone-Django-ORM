# https://docs.djangoproject.com/en/4.0/ref/models/fields/

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=None)
    age = models.IntegerField()
    birthday = models.DateField()
    email = models.EmailField()