from django.conf import settings
from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    capital_city = models.CharField(max_length=50)
    population = models.IntegerField()
    official_language = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
