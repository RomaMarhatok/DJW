from django.test import TestCase
from datetime import datetime
from wheather.models import City, DayCityWheather, HoursDayWheather


class TestCityModel(TestCase):
    def setUp(self):
        self.city = City.objects.create(name="London")

    def test_slug_field(self):
        self.assertEqual(self.city.slug, "london")


class TestDayCityWheatherModel(TestCase):
    def setUp(self) -> None:
        self.city1 = City.objects.create(name="London")
        self.city2 = City.objects.create(name="Moscow")
        self.wheather1 = DayCityWheather.objects.create(
            city=self.city1,
            date=datetime.now(),
            maxtemp_c=23.4,
            maxtemp_f=45.4,
            mintemp_c=12.2,
            mintemp_f=32.3,
            wind_kph=12,
            wind_degree=12,
            wind_dir="NEN",
            precip_mm=250,
            feelslike_c=34,
            condition_text="Sunny",
            icon_number=123,
        )
        self.wheather2 = DayCityWheather.objects.create(
            city=self.city2,
            date=datetime.now(),
            maxtemp_c=56,
            maxtemp_f=35,
            mintemp_c=65,
            mintemp_f=21,
            wind_kph=12,
            wind_degree=34,
            wind_dir="SES",
            precip_mm=250,
            feelslike_c=34,
            condition_text="Sunny",
            icon_number=123,
        )
        self.city1.save()
        self.city2.save()
        self.wheather1.save()
        self.wheather2.save()

    def test_mean_temp_c(self):
        self.assertEqual(self.wheather1.mean_temp_c(), 17.8)
        self.assertEqual(self.wheather1.mean_temp_f(), 38.85)

        self.assertEqual(self.wheather2.mean_temp_c(), 60.5)
        self.assertEqual(self.wheather2.mean_temp_f(), 28)

    def test_city_foreign_key(self):
        self.assertEqual(self.wheather1.city, self.city1)
        self.assertEqual(self.wheather2.city, self.city2)

    def test_writing_data(self):
        cities_count = City.objects.all().count()
        wheather_count = DayCityWheather.objects.all().count()
        self.assertEqual(cities_count, 2)
        self.assertEqual(wheather_count, 2)

    def test_delete_data(self):
        City.objects.all().delete()

        cities_count = City.objects.all().count()
        wheather_count = DayCityWheather.objects.all().count()

        self.assertEqual(cities_count, 0)
        self.assertEqual(wheather_count, 0)


class TestHoursDayWheather(TestCase):
    def setUp(self):
        self.city = City.objects.create(name="London")
        self.wheather = DayCityWheather.objects.create(
            city=self.city,
            date=datetime.now(),
            maxtemp_c=23.4,
            maxtemp_f=45.4,
            mintemp_c=12.2,
            mintemp_f=32.3,
            wind_kph=12,
            wind_degree=12,
            wind_dir="NEN",
            precip_mm=250,
            feelslike_c=34,
            condition_text="Sunny",
            icon_number=123,
        )
        self.data = {
            "day": self.wheather,
            "wind_kph": 16.9,
            "wind_degree": 80,
            "wind_dir": "E",
            "precip_mm": 0.0,
            "feelslike_c": 24.1,
            "condition_text": "Sunny",
            "icon_number": 113,
            "time": "2022-06-03 12:00",
            "temp_c": 11.4,
            "temp_f": 52.5,
        }

        self.hours_day_wheather = HoursDayWheather.objects.create(**self.data)

    def tes_foreign_keys(self):
        self.assertEqual(self.hours_day_wheather.day, self.wheather)
        self.assertEqual(self.hours_day_wheather.day.city, self.city)
