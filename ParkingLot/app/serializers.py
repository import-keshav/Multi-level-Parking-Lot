from rest_framework import serializers

from . import models


class ParkingLotSerializer(serializers.ModelSerializer):
    """Serializer for ParkingLot Model."""

    class Meta:
        model = models.ParkingLot
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    """Serializer for ParkingLot Model."""
    parking_lot = ParkingLotSerializer()

    class Meta:
        model = models.Ticket
        fields = '__all__'