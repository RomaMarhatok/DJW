from django.db import models


class WheatherMixin(models.Model):
    wind_kph = models.FloatField("maximum wind speed in kilometer per hour")
    wind_dir = models.CharField(
        "Wind direction as 16 point compass",
        max_length=10,
    )
    wind_degree = models.FloatField("wind direction in degrees")
    precip_mm = models.FloatField("precipitation amount in millimeters")
    feelslike_c = models.FloatField("feels like temperature as celcius")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WheatherConditionMixin(models.Model):
    condition_text = models.TextField("condition text")
    icon_number = models.PositiveIntegerField("number of icon")

    class Meta:
        abstract = True


class City(models.Model):
    name = models.CharField("name", max_length=200)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        db_table = "cities"


class DayCityWheather(WheatherMixin, WheatherConditionMixin):
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    date = models.DateField("wheather date")
    maxtemp_c = models.FloatField("max temp celsius")
    maxtemp_f = models.FloatField("max temp fahrenheit")
    mintemp_c = models.FloatField("min temp celsius")
    mintemp_f = models.FloatField("min temp fahrenheit")

    def mean_temp_c(self) -> float:
        return round((self.maxtemp_c + self.mintemp_c) / 2, 2)

    def mean_temp_f(self) -> float:
        return round((self.maxtemp_f + self.mintemp_f) / 2, 2)

    class Meta:
        db_table = "days"


class HoursDayWheather(WheatherMixin, WheatherConditionMixin):
    day = models.ForeignKey("DayCityWheather", on_delete=models.CASCADE)
    time = models.DateTimeField("wheather time")
    temp_c = models.FloatField("temp celsius")
    temp_f = models.FloatField("temp fahrenheit")

    class Meta:
        db_table = "hours"
