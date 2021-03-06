from django.db import models


class WeatherData(models.Model):
    country = models.CharField(max_length=50)
    year = models.IntegerField()
    month_or_season = models.CharField(max_length=3)
    reading_type = models.CharField(max_length=100)
    reading = models.FloatField(null=False)

    class Meta:
        unique_together = (("country",
                            "month_or_season",
                            "year",
                            "reading_type"))

    def __str__(self):
        return f"{self.country} - {self.year}"
