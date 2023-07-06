from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    profession = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.lastname} - {self.name}"
