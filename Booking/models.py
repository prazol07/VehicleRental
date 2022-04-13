from email.policy import default
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class VehicleRent(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    owner_name=models.CharField(max_length=100)
    vehicle_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    vehiclenumber=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=100)
    vehicle_image=models.ImageField(upload_to="uploads/")
    bluebook_image=models.ImageField(upload_to="uploads/bluebooks")
    price_per_day=models.IntegerField()
    phone=models.BigIntegerField()
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return self.vehicle_name

class VehicleBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    rent_info=models.ForeignKey(VehicleRent, on_delete=models.CASCADE, null=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    renting_days=models.IntegerField()
    date=models.DateField(max_length=100)

    







