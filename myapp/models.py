import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.

class Mechanic(models.Model):
    mid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=11)
    address=models.CharField(max_length=255)
    vehicle=models.CharField(max_length=255)
    specialization=models.CharField(max_length=255)
    yoe=models.CharField(max_length=3, verbose_name='Year of Experience')

class Booking(models.Model):
    bid=models.AutoField(primary_key=True)
    brand=models.CharField(max_length=255)
    modelname=models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='Book By')
    mechanic=models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='mechanic', verbose_name='Mechanic')
    serviceDescriptions=models.TextField(verbose_name='Description')
    bookingDate=models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Book Date')
    servicingDate=models.DateField(verbose_name='Service Date')
    mobile=models.CharField(max_length=10, validators=[MinLengthValidator(10)], verbose_name='Client Mobile')




