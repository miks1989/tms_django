from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.SmallIntegerField()
