from django.shortcuts import render
from vehicle_app.models import Vehicle

# Create your views here.
def Vehicle_Management(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'MainPage_vehicle.html', {'vehicles':vehicles})
