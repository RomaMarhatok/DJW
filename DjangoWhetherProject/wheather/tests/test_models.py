from wheather.models import City, DayCityWheather, HoursDayWheather
import pytest


@pytest.mark.django_db
def test_writing_delete_data(hour_factory):

    hour_factory.create()
    cities_count = City.objects.all().count()
    wheather_count = DayCityWheather.objects.all().count()
    hour_count = HoursDayWheather.objects.all().count()

    assert cities_count == 1
    assert wheather_count == 1
    assert hour_count == 1

    City.objects.all().delete()
    cities_count = City.objects.all().count()
    wheather_count = DayCityWheather.objects.all().count()
    hour_count = HoursDayWheather.objects.all().count()

    assert cities_count == 0
    assert wheather_count == 0
    assert hour_count == 0
