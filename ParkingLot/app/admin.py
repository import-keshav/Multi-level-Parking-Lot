from django.contrib import admin

from . import models

@admin.register(models.ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.ParkingLot._meta.fields]
