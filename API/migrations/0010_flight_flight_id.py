# Generated by Django 2.0.1 on 2018-04-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_remove_flight_flight_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
