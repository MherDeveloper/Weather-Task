from django.contrib import admin
from .models import WeatherData


@admin.register(WeatherData)
class AdminWeatherData(admin.ModelAdmin):

    list_display = ("country",
                    "year",
                    "month_or_season",
                    "reading_type",
                    "reading",
    )
    list_display_links = (
        "country",
        "year")