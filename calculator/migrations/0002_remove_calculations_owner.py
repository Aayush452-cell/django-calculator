# Generated by Django 4.0.2 on 2022-02-10 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculations',
            name='owner',
        ),
    ]
