from django.db import models

# Create your models here.


class Location (models.Model) :
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Company (models.Model) :
    name = models.CharField(max_length=200)
    contactNumber = models.CharField(max_length=15)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE, blank= False, null= False)
    
class User (models.Model) :
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE, blank = True, null = True)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE, blank= True, null= True)
    createdAt = models.DateTimeField(auto_now_add=True)

class Password (models.Model) :
    userId = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=64)
    changedAt = models.DateTimeField(auto_now=True)

