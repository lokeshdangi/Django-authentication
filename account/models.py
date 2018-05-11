from django.db import models
from django.utils import timezone

"""
class Address(models.Model):
    UserCity = models.CharField(max_length = 256)
    UserState = models.CharField(max_length = 256)
    UserCountry = models.CharField(max_length = 256)
    UserZip = models.CharField(max_length = 256)
 
class UserDetails(models.Model):
    UserFirstName= models.CharField(max_length = 256,blank=True)
    UserLastName = models.CharField(max_length = 256,blank=True)
    UserRegistrationDate = models.DateTimeField(default=timezone.now, editable=False)
    UserIP = models.CharField(max_length = 256,blank=True)
    UserPhone = models.CharField(max_length = 256,blank=True)
    UserAddress = models.ForeignKey(Address, on_delete=models.CASCADE,blank=True)
    
"""

class User(models.Model):
    UserEmail = models.EmailField(max_length = 256,unique=True)
    UserPassword = models.CharField(max_length = 256)
    
    """
    UserDetailsFor = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    
    """
        


    






    