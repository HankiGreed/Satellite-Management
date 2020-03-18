from satellites.models import Satellite, Organisation
from rest_framework import serializers


class satelliteSerializer(serializers.Serializer):
    Name = serializers.CharField()
    OrganisationName = serializers.CharField()
    CountryOrigin = serializers.CharField()
    Purpose = serializers.CharField()
    ClassOfOrbit = serializers.CharField()
    Perigee = serializers.IntegerField()
    Apogee = serializers.IntegerField()
    Inclination = serializers.FloatField()
    TimePeriod = serializers.FloatField()
    Power = serializers.IntegerField()
    Mass = serializers.IntegerField()
    DateOfLaunch = serializers.DateField()
    LifeSpan = serializers.IntegerField()
    LaunchVehicle = serializers.CharField()


class orgSerializer(serializers.Serializer):
    Name = serializers.CharField()
    CountryOperation = serializers.CharField()
    Purpose = serializers.CharField()
    UseCase = serializers.CharField()
    EmployeeCount = serializers.IntegerField()


class imageSerializer(serializers.Serializer):
    AbsolutePath = serializers.CharField()
    SatelliteName = serializers.CharField()
    Source = serializers.CharField()
    Description = serializers.CharField()
    DescribedBy = serializers.CharField()
    AssociatedReasearch = serializers.CharField()
