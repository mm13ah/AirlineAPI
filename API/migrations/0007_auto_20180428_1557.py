# Generated by Django 2.0.1 on 2018-04-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20180428_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_provider',
            old_name='login_password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='payment_provider',
            old_name='login_name',
            new_name='username',
        ),
    ]
