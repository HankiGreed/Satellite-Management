from django.contrib import admin
from .models import Profile, Satellite, Organisation

# Register your models here.

admin.site.register(Satellite)
admin.site.register(Organisation)
admin.site.register(Profile)
