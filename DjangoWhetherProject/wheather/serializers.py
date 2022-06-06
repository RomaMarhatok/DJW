from rest_framework import serializers
from wheather.models import City, DayCityWheather, HoursDayWheather
from datetime import datetime
from django.template.defaultfilters import slugify


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name", "slug"]


class DayCityWheatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayCityWheather
        exclude = ["updated_at", "created_at"]


class HourDayWheatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoursDayWheather
        exclude = ["updated_at", "created_at"]

    def get_hours(self, str_date: str) -> int | None:
        try:
            full_date_format = "%Y-%m-%d %H:%M"
            hour_format = "%H:%M"
            if self.__validate(str_date, full_date_format):
                return datetime.strptime(str_date, full_date_format).hour
            else:
                return datetime.strptime(str_date, hour_format).hour

        except ValueError:
            return None

    def __validate(self, str_date, format_str) -> bool:
        try:
            datetime.strptime(str_date, format_str)
            return True
        except ValueError:
            return False
