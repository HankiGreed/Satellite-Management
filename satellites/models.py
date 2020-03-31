from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organisation(models.Model):
    Name = models.CharField(max_length=200)
    CountryOperation = models.CharField(max_length=200)
    Purpose = models.CharField(max_length=200)
    UseCase = models.CharField(max_length=200)
    EmployeeCount = models.IntegerField(default=0)


def returnSatelliteFile(instance, filename):
    return "satellite_pic/Organisation_{0}/{1}".format(instance.Name, filename)


class Satellite(models.Model):
    Name = models.CharField(max_length=200, primary_key=True)
    Organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True
    )
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
    Description = models.CharField(max_length=300, null=True)
    Picture = models.ImageField(upload_to=returnSatelliteFile, null=True)


def returnUsersName(instance, filename):
    return "profile_pics/User_{0}/{1}".format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    EmployeID = models.CharField(max_length=25)
    AssociatedSat = models.OneToOneField(
        Satellite, on_delete=models.SET_NULL, null=True
    )
    Address = models.CharField(max_length=150)
    WorkExperience = models.CharField(max_length=100)
    WorkExperienceDesc = models.CharField(max_length=250, null=True)
    Organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True
    )
    Education1 = models.CharField(max_length=100, null=True)
    Education1_desc = models.CharField(max_length=250, null=True)
    Education2 = models.CharField(max_length=100, null=True)
    Education2_desc = models.CharField(max_length=250, null=True)
    Education3 = models.CharField(max_length=100, null=True)
    Education3_desc = models.CharField(max_length=250, null=True)
    is_head = models.BooleanField(default=False)
    Profile_pic = models.ImageField(upload_to=returnUsersName, null=True)
