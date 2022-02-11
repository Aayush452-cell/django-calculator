# Generated by Django 4.0.2 on 2022-02-10 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_userprofile_calculations'),
        ('calculator', '0004_alter_calculations_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculations',
            name='owner',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile'),
        ),
    ]
