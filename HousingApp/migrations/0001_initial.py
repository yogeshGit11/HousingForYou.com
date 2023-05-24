# Generated by Django 4.2 on 2023-05-23 10:13

import HousingApp.current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='HouseOnSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_photos', models.ImageField(upload_to='HouseOnSalePhotos/')),
                ('about_house', models.CharField(max_length=700)),
                ('house_location', models.CharField(max_length=150)),
                ('city_name', models.CharField(max_length=100)),
                ('Owner_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('house_price', models.CharField(max_length=20)),
                ('house_type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='HousingApp.housetype')),
                ('user_name', models.ForeignKey(default=HousingApp.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HouseOnRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_photos', models.ImageField(upload_to='HouseOnRentPhotos/')),
                ('about_house', models.CharField(max_length=700)),
                ('house_location', models.CharField(max_length=150)),
                ('city_name', models.CharField(max_length=100)),
                ('Owner_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('house_rent', models.CharField(max_length=20)),
                ('house_type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='HousingApp.housetype')),
                ('user_name', models.ForeignKey(default=HousingApp.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
