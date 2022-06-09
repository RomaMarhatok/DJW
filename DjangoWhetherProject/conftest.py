import pytest
from pytest_factoryboy import register
from wheather.tests.factories import (
    CityFactory,
    DayFactory,
    HourFactory,
)
from django.template.defaultfilters import slugify
from faker import Faker
from wheather.models import DayCityWheather, HoursDayWheather, City

register(CityFactory)
register(DayFactory)
register(HourFactory)


fake = Faker()


@pytest.fixture
def city_fixture():
    name = fake.city()
    slug = slugify(name)
    data = {"name": name, "slug": slug}
    return City.objects.create(**data)


@pytest.fixture
def day_fixture(city_fixture):
    data = {
        "city": city_fixture,
        "date": fake.date(),
        "wind_kph": fake.pyfloat(left_digits=2, right_digits=2),
        "wind_degree": fake.pyfloat(left_digits=2, right_digits=2),
        "wind_dir": fake.pystr(max_chars=10),
        "precip_mm": fake.pyfloat(left_digits=2, right_digits=3, positive=True),
        "feelslike_c": fake.pyfloat(left_digits=2, right_digits=2),
        "condition_text": fake.date(),
        "icon_number": fake.pyint(),
        "maxtemp_c": fake.pyfloat(left_digits=2, right_digits=2),
        "maxtemp_f": fake.pyfloat(left_digits=2, right_digits=2),
        "mintemp_c": fake.pyfloat(left_digits=2, right_digits=2),
        "mintemp_f": fake.pyfloat(left_digits=2, right_digits=2),
    }
    return DayCityWheather.objects.create(**data)


@pytest.fixture
def hour_fixture(day_fixture):
    data = {
        "day": day_fixture,
        "wind_kph": fake.pyfloat(left_digits=2, right_digits=2),
        "wind_degree": fake.pyfloat(left_digits=2, right_digits=2),
        "wind_dir": fake.pystr(max_chars=10),
        "precip_mm": fake.pyfloat(left_digits=2, right_digits=3, positive=True),
        "feelslike_c": fake.pyfloat(left_digits=2, right_digits=2),
        "condition_text": fake.date(),
        "icon_number": fake.pyint(),
        "time": fake.date_object(),
        "temp_c": fake.pyfloat(left_digits=2, right_digits=2),
        "temp_f": fake.pyfloat(left_digits=2, right_digits=2),
    }
    return HoursDayWheather.objects.create(**data)
