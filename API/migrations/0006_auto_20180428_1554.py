# Generated by Django 2.0.1 on 2018-04-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20180422_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_provider',
            name='login_name',
            field=models.CharField(default='mm13ah', max_length=10),
        ),
        migrations.AddField(
            model_name='payment_provider',
            name='login_password',
            field=models.CharField(default='badpassword', max_length=20),
        ),
    ]
