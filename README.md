# iot-workspace-management
Sample use case for workspace management based on IOX Gateway

## Sample Code Description:
This is an end to end sample project for managing the workspace using sensors deployed in the office cubicles. A fog application running on the IOX gateway collects the sensor data which is sent to a centralized server application which provides a dashboard of workspace usage in real time.

## Component Design:
### Sensors	Simulation
* Client Application simulates a proximity sensor payload and sends to IOX  (Fog) Application

### Gateway Application	
* IOX Application will receive the user presence json data from the sensor
* Fog Application will run on the IOX gateway within a container of its own	
* IOT Fog Application will receive the user presence json data from the sensor and apply business logic to improve / optimize the data transfer

### Server Application	
* Sensors will register with Server Application 
* Application will receive the user presence json data from the sensor
* Application will update the transaction tables  with sensor data
* Display the status of the user presence on the office floor layout

### Database	
* Holds a sample schema for Bldg,Floor,Cubicle,Sensor data (sl no, type, value)
* The database stores the status of all sensors and will display on the dashboard.

## Technologis:
Python3
requests
flask
HTML
AngularJs
MySQL
adapter

## How to Get Started:
* clone this repo

## Result:



