from django.db import models
from datetime import date
class UserCredentials(models.Model):
    email = models.EmailField(unique=True)
    mob = models.CharField(max_length=15, unique=True, blank=True, null=True)
    pwd = models.CharField(max_length=100)

class UserDetails(models.Model):
    user_credentials = models.OneToOneField(UserCredentials, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    profile_image_path = models.CharField(max_length=255, blank=True, null=False)
    occupation = models.CharField(max_length=50)
    m_s = models.CharField(max_length = 20)
    income = models.CharField(max_length = 100)
    savings = models.IntegerField(default=0)
class Expense(models.Model):
    user_id = models.CharField(max_length = 20,default=0)
    pre_category = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(default = date.today)
