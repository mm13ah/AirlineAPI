# Generated by Django 2.0.1 on 2018-04-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20180414_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='passengers',
        ),
        migrations.AddField(
            model_name='booking',
            name='passengers',
            field=models.ManyToManyField(to='API.Passenger'),
        ),
    ]
