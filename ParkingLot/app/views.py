from datetime import datetime, timezone

from django import forms
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, status, filters
from rest_framework.renderers import JSONRenderer

from . import models
from . import serializers


class ParkingLot(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        '''
            Handling GET request on the particular url.

        Args:
            request obj: Request Object.

        Returns;
            Response obj: Returns Django Response opbject.
        '''

        return  Response(
            [serializers.ParkingLotSerializer(slot).data for slot in models.ParkingLot.objects.filter(is_occupied=False)])


    def post(self, request):
        '''
            Handling POST request on the particular url.

        Args:
            request obj: Request Object.

        Returns;
            Response obj: Returns Django Response opbject.
        '''
        if not 'vehicle_num' in self.request.data:
            return Response({
                "message": "include vehicle_num in data"
            }, status=status.HTTP_400_BAD_REQUEST)

        if models.Ticket.objects.filter(car_no=self.request.data['vehicle_num']).count() >=1:
            return Response({
                "message": "Vehicle already present in Parking Lot"
            }, status=status.HTTP_400_BAD_REQUEST)


        queryset = models.ParkingLot.objects.filter(is_occupied=False)
        if not queryset.count():
            return Response(status=status.HTTP_200_OK)

        parking_lot = queryset.first()
        ticket = models.Ticket(
                parking_lot=parking_lot,
                car_no=self.request.data['vehicle_num']
            )
        ticket.save()

        parking_lot.is_occupied = True
        parking_lot.save()

        return Response(serializers.TicketSerializer(ticket).data,
                status=status.HTTP_201_CREATED
            )


class ExitParkingLot(APIView):
    def post(self, request, ticket_id):
        '''
            Handling POST request on the particular url.

        Args:
            request obj: Request Object.

        Returns;
            Response obj: Returns Django Response opbject.
        '''
        ticket = models.Ticket.objects.filter(id=ticket_id).first()

        if not ticket:
            return Response({
                "message": "No Ticket exist with this ID"
            }, status=status.HTTP_400_BAD_REQUEST)

        total_amount = ((
            datetime.now(timezone.utc) - ticket.entry_time
        ).total_seconds() / 60) * 0.1

        ticket.delete()
        return Response({
                "total_amount": total_amount 
            }, status=status.HTTP_200_OK)
