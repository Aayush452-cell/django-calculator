# Generated by Django 4.0.2 on 2022-02-10 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_remove_calculations_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculations',
            name='entries',
        ),
    ]
