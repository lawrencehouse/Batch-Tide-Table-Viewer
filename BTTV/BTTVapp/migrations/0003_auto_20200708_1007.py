# Generated by Django 3.0.6 on 2020-07-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTTVapp', '0002_auto_20200708_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.CharField(max_length=200),
        ),
    ]
