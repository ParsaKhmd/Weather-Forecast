from django.db import models

# Create your models here.

from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    temperature = models.FloatField()
    condition = models.CharField(max_length=255)
    humidity = models.FloatField()
    icon_url = models.URLField(null=True)

    def __str__(self):
        return f"{self.city}, {self.country}"
