from django.urls import path

from . import views
from . import services


urlpatterns = [
	path('parking-spots', views.ParkingLot.as_view()),
	path('parking-spots/<int:ticket_id>/exit', views.ExitParkingLot.as_view()),
]


services.initialize_parking_slots()
