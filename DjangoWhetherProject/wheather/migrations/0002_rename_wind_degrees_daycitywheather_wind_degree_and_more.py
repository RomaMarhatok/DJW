# Generated by Django 4.0.5 on 2022-06-03 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wheather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daycitywheather',
            old_name='wind_degrees',
            new_name='wind_degree',
        ),
        migrations.RenameField(
            model_name='hoursdaywheather',
            old_name='wind_degrees',
            new_name='wind_degree',
        ),
    ]
