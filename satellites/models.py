from django.db import models

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


class Employee(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=200)
    Address = models.CharField(max_length=500)
    AssociatedSat = models.CharField(max_length=500)


class Images(models.Model):
    AbsolutePath = models.CharField(max_length=200)
    SatelliteName = models.CharField(max_length=500)
    Source = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    DescribedBy = models.CharField(max_length=500)
    AssociatedReasearch = models.CharField(max_length=200)
