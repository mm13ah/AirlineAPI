# Generated by Django 2.0.1 on 2018-04-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_auto_20180428_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_id',
            field=models.CharField(default=1, max_length=5, unique=True),
            preserve_default=False,
        ),
    ]
