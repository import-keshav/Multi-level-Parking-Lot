# Multi-level-Parking-Lot.
Backend Assignment

<h4> TechStack Used</h4>
1. Python (Programming Language)<br>
2. Django (Web Framework)<br>
3. Sqlite (Database)<br>


<h5> API's Postman ScreenShots</h5>
<h6> Book ParkingLot (POST Request)</h6>
API for booking ParkingLot
<img src="https://user-images.githubusercontent.com/34139754/105572902-ee967680-5d7f-11eb-9ccf-0ffffd8bd8e6.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 201 OK  |   673ms |    374 B    |


<h6> GET ParkingLot (GET Request)</h6>
API for getting ParkingLot
<img src="https://user-images.githubusercontent.com/34139754/105572884-d4f52f00-5d7f-11eb-9025-a41b4083e370.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 200 OK  |   50 ms |    7.98 KB  |


<h6> Exit ParkingLot (POST Request)</h6>
API for exit ParkingLot
<img src="https://user-images.githubusercontent.com/34139754/105572883-d32b6b80-5d7f-11eb-9d95-57c40349a62a.png">

| Status  |   Time  |    Size     |
| ------- | ------- | ------------|
| 200 OK  |   421ms |    254 B    |


<h5> How to setup and run locally </h5>
<p>
  1. Clone the Repository <br>
  2. <a href="https://www.geeksforgeeks.org/python-virtual-environment/"> Create a Activate Python Virtual Environment </a></h5><br>
  3. After activating the virtual enviornment, redirect to project base directory. <br>
  4. Run the following command for installing dependencies.
</p>

    $ pip3 install -r requirements.txt

<br>
  5. Now direct to TeamWave folder for starting the django server.

    $ cd Multi-level-Parking-Lot.

<br>
  6. Now before running the server, we have to setup database, so run.
 
    $ python3 manage.py migrate

<br>
  7. Now run the following command for starting the server

    $ python3 manage.py runserver

<br>

Now run the following api described in the above Postman image.
<br>

