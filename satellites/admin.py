from django.contrib import admin
from .models import Satellite, Organisation, Employee, Images

# Register your models here.

admin.site.register(Satellite)
admin.site.register(Organisation)
admin.site.register(Employee)
admin.site.register(Images)
