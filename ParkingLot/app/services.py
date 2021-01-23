from . import models

def initialize_parking_slots():
	if models.ParkingLot.objects.all().count() == 125:
		return

	for floor_num in range(1,6):
		for row_num in range(1,6):
			for col_num in range(1,6):
				obj = models.ParkingLot(
						floor_no=floor_num,
						row_no=row_num,
						col_no=col_num
					)
				obj.save()
