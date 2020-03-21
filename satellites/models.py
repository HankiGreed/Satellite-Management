from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Satellite(models.Model):
    Name = models.CharField(max_length=200, primary_key=True)
    OrganisationName = models.CharField(max_length=200)
    CountryOrigin = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    ClassOfOrbit = models.CharField(max_length=200)
    Perigee = models.IntegerField()
    Apogee = models.IntegerField()
    Inclination = models.FloatField()
    TimePeriod = models.FloatField()
    Power = models.IntegerField()
    Mass = models.IntegerField()
    DateOfLaunch = models.DateField()
    LifeSpan = models.IntegerField()
    LaunchVehicle = models.CharField(max_length=200)


class Organisation(models.Model):
    Name = models.CharField(max_length=200)
    CountryOperation = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    UseCase = models.CharField(max_length=200)
    EmployeeCount = models.IntegerField(default=0)


class Images(models.Model):
    AbsolutePath = models.CharField(max_length=200)
    SatelliteName = models.CharField(max_length=500)
    Source = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    DescribedBy = models.CharField(max_length=500)
    AssociatedReasearch = models.CharField(max_length=200)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    EmployeID = models.CharField(max_length=25)
    AssociatedSat = models.OneToOneField(Satellite, on_delete=models.SET_NULL, null=True)
    Address = models.CharField(max_length=150)
    WorkExperience = models.CharField(max_length=100)
    Education = models.CharField(max_length=100)
