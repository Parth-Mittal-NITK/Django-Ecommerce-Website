from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) #A model that extends the exitsing user model
    addressline = models.CharField(max_length=100 , default="")
    city = models.CharField(max_length=50 , default="")
    state = models.CharField(max_length=50 , default="")
    zip_code = models.CharField(max_length=10 , default="")
    phone = models.CharField(max_length=12 , default="")