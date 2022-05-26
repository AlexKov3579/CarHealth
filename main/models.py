from django.db import models
from login import models as login_models

# Create your models here.

class Car(models.Model):
    userId = models.ForeignKey(login_models.User, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    kilometrage = models.IntegerField()
    year = models.IntegerField()
    checkDate = models.DateField()
    nextCheckDate = models.DateField()
    fuel = models.CharField(max_length=30, default="Dīzelis")
    engineVol = models.FloatField(default=1.5)
    def natural_key(self):
        return(self.manufacturer, self.model, self.year)

class PartsType(models.Model):

    ConditionMeasurment = [
        ('KM', 'Kilometres'),
        ('MI', 'Miles'),
        ('Time', 'Time'),
        ('L', 'Volume')
    ]

    typeName = models.CharField(max_length=50)
    conditionMeasurment = models.CharField(max_length=5, choices=ConditionMeasurment, default='KM')
    stockCondition = models.FloatField()
    def natural_key(self):
        return (self.typeName, self.conditionMeasurment)



class Part(models.Model):
    carId = models.ForeignKey(Car, on_delete=models.CASCADE)
    serial = models.CharField(max_length=100,null=True)
    typeId = models.ForeignKey(PartsType, on_delete=models.CASCADE)
    manufacterDate = models.DateField(null=True)
    currentCondition = models.FloatField()
    additionalInfo = models.JSONField(null=True)

