import pytest
from wheather.models import City, DayCityWheather, HoursDayWheather
from wheather.serializers import (
    CitySerializer,
    DayCityWheatherSerializer,
    HourDayWheatherSerializer,
)


@pytest.mark.django_db
def test_city_serialization(city_factory, day_factory):

    city = city_factory.build()
    serializer_data = {"name": city.name, "slug": city.slug}
    serializer = CitySerializer(data=serializer_data)
    serializer.is_valid()
    serializer.save()
    cities_count = City.objects.all().count()

    assert cities_count == 1


@pytest.mark.django_db
def test_day_serialization(day_fixture):
    DayCityWheatherSerializer(instance=day_fixture)
    day_count = DayCityWheather.objects.all().count()
    assert day_count == 1


@pytest.mark.django_db
def test_hour_serialization(hour_fixture):
    HourDayWheatherSerializer(instance=hour_fixture)
    hour_count = HoursDayWheather.objects.all().count()

    assert hour_count == 1


@pytest.mark.django_db
def test_get_hours(hour_fixture):
    serializer = HourDayWheatherSerializer(instance=hour_fixture)
    times = ["2022-06-03 00:00", "2022-06-03 23:00", "", "09:00"]
    assert serializer.get_hours(times[0]) == 0
    assert serializer.get_hours(times[1]) == 23
    assert serializer.get_hours(times[2]) is None
    assert serializer.get_hours(times[3]) == 9
