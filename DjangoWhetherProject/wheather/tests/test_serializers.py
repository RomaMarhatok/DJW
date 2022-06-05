from django.test import TestCase
from wheather.models import City, DayCityWheather
from wheather.serializers import (
    CitySerializer,
    DayCityWheatherSerializer,
    HourDayWheatherSerializer,
)


class TestCitySerializer(TestCase):
    def setUp(self):
        self.serializer_data = {"name": "London"}

        self.serializer = CitySerializer(data=self.serializer_data)

    def test_data_serialization(self):
        serializer = CitySerializer(data=self.serializer_data)
        serializer.is_valid()
        self.assertEqual(serializer.data, self.serializer_data)

    def test_object_serialization(self):
        city = City.objects.create(**self.serializer_data)
        serializer = CitySerializer(instance=city)
        self.assertEqual(serializer.data["name"], self.serializer_data["name"])

    def test_serialization_errors(self):
        bad_serializer_data = {"name": None}
        serializer = CitySerializer(data=bad_serializer_data)
        serializer.is_valid()
        self.assertEqual(set(serializer.errors), set(["name"]))

    def test_serialization(self):
        self.serializer.is_valid()
        self.serializer.save()
        city = City.objects.get(pk=1)
        self.assertEqual(City.objects.all().count(), 1)
        self.assertEqual(city.slug, "london")


class TestDayCityWheatherSerializer(TestCase):
    def setUp(self):
        self.city1 = City.objects.create(name="London")
        self.serializer_data = {
            "city": self.city1.pk,
            "date": "2022-06-03",
            "wind_kph": 16.9,
            "wind_degree": 80,
            "wind_dir": "E",
            "precip_mm": 0.0,
            "feelslike_c": 24.1,
            "condition_text": "Sunny",
            "icon_number": 113,
            "maxtemp_c": 21.5,
            "maxtemp_f": 70.7,
            "mintemp_c": 10.3,
            "mintemp_f": 50.5,
        }

        self.bad_serializer_data = {
            "city": self.city1.pk,
            "date": "2022-06-03",
            "wind_kph": 16.9,
            "wind_degree": 80,
            "wind_dir": "E",
            "precip_mm": "",
            "feelslike_c": "",
            "condition_text": "Sunny",
            "icon_number": 113,
            "maxtemp_c": 21.5,
            "maxtemp_f": 70.7,
            "mintemp_c": 10.3,
            "mintemp_f": 50.5,
        }

    def test_serialization(self):
        serializer = DayCityWheatherSerializer(data=self.serializer_data)
        serializer.is_valid()
        self.assertEqual(set(serializer.data.keys()), set(self.serializer_data.keys()))

    def test_serialization_errors(self):
        serializer = DayCityWheatherSerializer(data=self.bad_serializer_data)
        serializer.is_valid()
        self.assertEqual(set(serializer.errors), set(["precip_mm", "feelslike_c"]))

    def test_save(self):
        serializer = DayCityWheatherSerializer(data=self.serializer_data)
        serializer.is_valid()
        serializer.save()
        self.assertEqual(DayCityWheather.objects.all().count(), 1)


class TestHourDayWheatherSerializer(TestCase):
    def setUp(self):
        self.serializer_data = {
            "day": 1,
            "wind_kph": 16.9,
            "wind_degree": 80,
            "wind_dir": "E",
            "precip_mm": 0.0,
            "feelslike_c": 24.1,
            "condition_text": "Sunny",
            "icon_number": 113,
            "time": "2022-06-03 00:00",
            "temp_c": 11.4,
            "temp_f": 52.5,
        }
        self.serializer = HourDayWheatherSerializer(data=self.serializer_data)

    def test_serialization(self):
        self.serializer.is_valid()
        self.assertEqual(
            set(self.serializer.data.keys()), set(self.serializer_data.keys())
        )

    def test_get_hours(self):
        times = ["2022-06-03 00:00", "2022-06-03 23:00", "", "09:00"]
        self.assertEqual(self.serializer.get_hours(times[0]), 0)
        self.assertEqual(self.serializer.get_hours(times[1]), 23)
        self.assertEqual(self.serializer.get_hours(times[2]), None)
        self.assertEqual(self.serializer.get_hours(times[3]), 9)
