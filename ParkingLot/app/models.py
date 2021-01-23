from django.db import models

class ParkingLot(models.Model):
    floor_no = models.IntegerField()
    row_no = models.IntegerField()
    col_no = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'ParkingLot'
        verbose_name_plural = 'ParkingLots'


class Ticket(models.Model):
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, related_name="parking_lot")
    car_no = models.CharField(max_length=20)
    entry_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
