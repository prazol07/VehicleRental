from django.contrib import admin

from Booking.models import VehicleBook, VehicleRent

# Register your models here.
admin.site.register(VehicleBook)
admin.site.register(VehicleRent)