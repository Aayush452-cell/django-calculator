# Generated by Django 4.0.2 on 2022-02-10 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0004_initial'),
        ('calculator', '0011_delete_calculations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('entries', models.CharField(max_length=150)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile')),
            ],
        ),
    ]
