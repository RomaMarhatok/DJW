from django.test import TestCase
from datetime import datetime
from wheather.models import City, DayCityWheather


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
