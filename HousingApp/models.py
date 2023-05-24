from django.db import models
from django.contrib.auth.models import User
from HousingApp import current_user
from datetime import date

class HouseType(models.Model):
    roomtype=models.CharField(max_length=40)

    def __str__(self):
        return self.roomtype
    
class HouseOnRent(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=current_user.get_current_user)
    house_photos=models.ImageField(upload_to='HouseOnRentPhotos/')
    house_type=models.ForeignKey(HouseType,on_delete=models.CASCADE,default='')
    about_house=models.CharField(max_length=700)
    house_location=models.CharField(max_length=150)
    city_name=models.CharField(max_length=100)
    Owner_name=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=10)
    house_rent=models.CharField(max_length=20)
    publish_date=models.DateField(default=date.today)

class HouseOnSell(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=current_user.get_current_user)
    house_photos=models.ImageField(upload_to='HouseOnSalePhotos/')
    house_type=models.ForeignKey(HouseType,on_delete=models.CASCADE,default='')
    about_house=models.CharField(max_length=700)
    house_location=models.CharField(max_length=150)
    city_name=models.CharField(max_length=100)
    Owner_name=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=10)
    house_price=models.CharField(max_length=20)
    publish_date=models.DateField(default=date.today)