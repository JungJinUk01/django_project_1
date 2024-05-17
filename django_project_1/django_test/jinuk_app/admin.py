from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'vehicle_num0', 'vehicle_num', 'vehicle_id')

admin.site.register(Vehicle, VehicleAdmin)

# Register your models here.
