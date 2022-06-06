import factory
from wheather.models import (
    City,
    DayCityWheather,
    HoursDayWheather,
    WheatherMixin,
    WheatherConditionMixin,
)
from django.template.defaultfilters import slugify
from faker import Faker

fake = Faker()


class WheatherMixinFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True
        model = WheatherMixin

    wind_kph = fake.pyfloat(left_digits=2, right_digits=2)
    wind_dir = fake.pystr(max_chars=10)
    wind_degree = fake.pyfloat(left_digits=2, right_digits=2)
    precip_mm = fake.pyfloat(left_digits=2, right_digits=3, positive=True)
    feelslike_c = fake.pyfloat(left_digits=2, right_digits=2)


class WheatherConditionMixinFactory(factory.django.DjangoModelFactory):
    condition_text = fake.text()
    icon_number = fake.pyint()

    class Meta:
        abstract = True
        model = WheatherConditionMixin


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = fake.city()
    slug = slugify(name)


class DayFactory(WheatherMixinFactory, WheatherConditionMixinFactory):
    class Meta:
        model = DayCityWheather

    city = factory.SubFactory(CityFactory)
    date = fake.date()
    maxtemp_c = fake.pyfloat(left_digits=2, right_digits=2)
    maxtemp_f = fake.pyfloat(left_digits=2, right_digits=2)
    mintemp_c = fake.pyfloat(left_digits=2, right_digits=2)
    mintemp_f = fake.pyfloat(left_digits=2, right_digits=2)


class HourFactory(WheatherMixinFactory, WheatherConditionMixinFactory):
    day = factory.SubFactory(DayFactory)
    time = fake.date_object()
    temp_c = fake.pyfloat(left_digits=2, right_digits=2)
    temp_f = fake.pyfloat(left_digits=2, right_digits=2)

    class Meta:
        model = HoursDayWheather
