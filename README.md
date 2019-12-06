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
![architecture](https://github.com/wiprodevnet/iot-workspace-management/blob/master/images/architecture.png)

### Server Application	
* Sensors will register with Server Application 
* Application will receive the user presence json data from the sensor
* Application will update the transaction tables  with sensor data
* Display the status of the user presence on the office floor layout

### Database	
* Holds a sample schema for Building,Floor,Cubicle,Sensor Data (sl no, type, value)
* The database stores the status of all sensors and will display on the dashboard.

## Technologies:
1. Python3
2. requests
3. Flask
4. HTML
5. AngularJs
6. MySQL
7. flask-mysql

## Installation and Configuration
### Steps to Set-up profile for ioxclient
1. reset profile first
   > ./ioxclient profiles reset
2. create profile
   > ./ioxclient  profiles create
   
		Creating one time configuration..
		Your / your organization's name : cisco
		Your / your organization's URL : cisco.com
		Your IOx platform's IP address[127.0.0.1] : 10.10.20.51
		Your IOx platform's port number[8443] : 8443
		Authorized user name[root] : cisco
		Password for cisco : 
		Local repository path on IOx platform[/software/downloads]: 
		URL Scheme (http/https) [https]: 
		API Prefix[/iox/api/v2/hosting/]: 
		Your IOx platform's SSH Port[2222]: 22
		Your RSA key, for signing packages, in PEM format[]: 
		Your x.509 certificate in PEM format[]: 
		Activating Profile  default
		Saving current configuration
		Active Profile :  default
		Enter a name for this profile : sandbox
		Your IOx platform's IP address[127.0.0.1] : 10.10.20.51
		Your IOx platform's port number[8443] : 8443
		Authorized user name[root] : cisco
		Password for cisco : 
		Local repository path on IOx platform[/software/downloads]: 
		URL Scheme (http/https) [https]: 
		API Prefix[/iox/api/v2/hosting/]: 
		Your IOx platform's SSH Port[2222]: 22
		Your RSA key, for signing packages, in PEM format[]: 
		Your x.509 certificate in PEM format[]: 
		Activating Profile  sandbox
		Saving current configuration

3.  Activate the profile
 > ./ioxclient  profiles activate sandbox

### Steps to create images 

  > git clone https://github.com/wiprodevnet/iot-workspace-management.git  
  > cd iot-workspace-management/IOXApp  
  > sudo docker build -t iot_sensor_data_app . 


### Steps to delopy docker images into IOx Fog Director
1. Reserve the IOx-CAF x2 + Fog Director under IOT section
2. After that connect the sandbox with anyconnect by using credential received in a mail.
3. Go to ioxclient folder
4. Package the IOx Application with the ioxclient tool
5. To create package
		> sudo ./ioxclient docker package iot_sensor_data_app .
6. To Deploy the IOX Application using ioxclient
		>./ioxclient application install IOT_WORKSPACE_MANAGEMENT_APP package.tar
7.  After that login into sandbox activate and start the app.

Step to run client to send sensor data to app.
 > cd sensorSimulation/
 > python3 client_v1.py

Steps to run webserver app to show dashboard
1. cd webServerApp/
2. python3 runserver.py
3. open Browser and paste this url http://0.0.0.0:9001/


## Installation and Configuration:
* Clone this repo first and follow the steps to run each Component.

## Steps to Deploy IOXApp

### Prerequisites
Previous IOx labs needed to complete this lab
You will need to have completed the learning the following labs:
1. Introduction to Cisco IOx - https://developer.cisco.com/learning/tracks/iot/IoT-IOx-Intro/intro-2-iox/step/1
2. Intro to Containers - https://developer.cisco.com/learning/tracks/iot/IoT-IOx-Apps/Containers-101/step/1
3. Intro to Docker - https://developer.cisco.com/learning/tracks/iot/IoT-IOx-Apps/docker-101/step/1

### Docker technologies
You should have a basic understanding on how to build and run a docker application.

### Docker Platform
To create a Docker image and push it to the Docker Hub, you will need the correct Docker tools for your platform which are available at https://www.docker.com/products/overview.
Download and install the correct version for your operating system.

### IOx Dev Environment As A Service 
This lab has instructions for using a docker container that sets up a web service you can access from your browser. The web service is a browser based version of Visual Studio Code, developed by Coder Com (https://coder.com) and utilizes docker to run the service. Since it is Visual Studio Code, it it provides a text/code editor and comes pre-built with ioxclient and everything you need to build IOx applications. You will need the Docker Platform on your desktop or developer machine to run this environment.

### Cisco AnyConnect Client
To access the DevNet Sandbox, you will need to use the Cisco AnyConnect Client for Virtual Private Network (VPN) access to the IOx instance. If you need to install it, you can find it at this link.

	Note: If you are working on a DevNet Lab workstation, this software is already installed.

### ioxclient
You will need the ioxclient to package and deploy the IOx Application. If you need to download it, you can find it at this link.
	Note: If you are working on a DevNet Lab workstation or you are using the "IOx Dev Environment As A Service" container, this software is already installed.

### git
One way to get the application template code is to use git. We have the option to download the code, so this step is optional. If you are working on a DevNet Lab workstation, the git software is already installed. If you need to install it, you can find it at this link.

	Note: You can verify the installation of git by opening a command prompt and running:

### git --version
	Additional Note: If you are working on a DevNet Lab workstation or you are using the "IOx Dev Environment As A Service" container, this software is already installed.

Once you have verified the prerequisites to complete this lab you will:

### Reserve an IOx Sandbox instance:- 
   1. Setup a Local Container for the IOx Developer Environment
   2. Create a small IOx Application to run on the Sandbox IOx device
   3. Package the IOx Application with the ioxclient Docker tools
   4. Connect to the DevNet Sandbox
   5. Deploy the IOx Application
   6. Monitor and review the IOx Application
   7. Test the output of the IOx Application

## Refer below link for more details
* https://developer.cisco.com/learning/modules/iox-basic/iot-iox-app-docker/step/1

## Steps to run sensorSimulation
1. Open sencors_data.py and configure the IOX sandbox external IP and port. 
2. Run below command to send sensor datat to IOXApp
	> python3 client_v1.py
## Steps to run webServerApp
   ### Prerequisites
1. Install Python3
   > Sudo apt-get install python3.6
2. Install all the necessary packages (best done inside of a virtual environment)
   > pip install -r requirements.txt 
3. Install MySql
   > sudo apt-get install mysql-server
4. Import Database in MySql and Configure Database details in main.py

Refer below link for more details about MYSql installtion
  https://vitux.com/how-to-install-and-configure-mysql-in-ubuntu-18-04-lts/
        
   ### Run below command to start Flask server
         $python3 runserver.py

## Smart WorkSpace UI:
 ### Smart WorkSpace Dashboard
 ![trackWorkSpace](https://github.com/wiprodevnet/iot-workspace-management/blob/master/images/trackWorkSpace.png)
 
 ### Smart WorkSpace Sensor Registoration Page
 ![registerSensor](https://github.com/wiprodevnet/iot-workspace-management/blob/master/images/registerSensor.png)





