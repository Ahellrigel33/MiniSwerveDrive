# Mini Swerve Drive
Project by Andrew Hellrigel and Ryan Chen

A swerve drive is a 4 wheeled robot where each wheel can be independently driven and steered. This allows the robot to be able to translate in any direction while also being able to rotate at the same time. We built a simple swerve drive robot using stepper motors as the steering motors and 550 DC motors as the drive motors for each module. Via wifi with an ESP8266, it connects to a computer that is running a python script to read an XBOX controller input and then send the commands.

[View a video of the swerve drive](https://youtu.be/719igPGglS0)

###### Swerve Drive Assembly
![mini_swerve_drive_pic](https://user-images.githubusercontent.com/57779689/165911164-4edecc34-d9fc-45f4-bdc5-43dedc971e39.jpg)

## Mechanical Design

#### CAD Model
View the [CAD Model](https://cad.onshape.com/documents/7647162e80dae337830eed48/w/d2e661ed10475200ea589299/e/53a591cb0b692bf025469395?renderMode=0&uiState=626ae1af2d4da8269f2dcc8e) on OnShape

###### Frame with One Module
![Frame](https://user-images.githubusercontent.com/31022165/165826054-c8084df3-d574-4f67-839c-04d820173075.png)

###### Single Swerve Module
![SwerveModule](https://user-images.githubusercontent.com/31022165/165826176-24a18222-53f3-4fd6-ac80-a75b8940235e.png)


#### Parts Needed
For the mechanical assembly, most of the parts can be 3D printed from the files located in the OnShape CAD model. However, there are a few extra parts that are needed as shown below.
- [Delrin for laser cutting gears](https://www.amazon.com/dp/B07GNLYSWT?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Deep grove ball bearings](https://www.amazon.com/dp/B088BJBWJ5?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [8mm ball bearings](https://www.amazon.com/dp/B07R7PR72H?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Aluminum square tube (20mm x 20mm x 200mm with 2mm wall)](https://www.amazon.com/dp/B07ZVS9KCR?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [GT2 synchronous timing pulleys (20t and 60t)](https://www.amazon.com/dp/B08DNLWQPM?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [8mm x 300mm linear motion rods](https://www.amazon.com/dp/B09P87MSY7?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [3.175mm to 5mm pinion reducer sleeve](https://www.amazon.com/dp/B08ZNC7YTD?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [20t bevel gears](https://www.amazon.com/dp/B01EUXS6KS?psc=1&ref=ppx_yo2ov_dt_b_product_details)

Additionally, some metric and standard hardware is needed for assembly (mostly M3, M4, and 6-32 screws and nuts are used)

## Electrical Design
The electrical design works with an MBED LPC1768 microcontroller as the main controller for the drivetrain. The MBED connects to 4 motor controllers, 4 stepper motor controllers, and a bluetooth module. For power, a 3S lipo battery and a 5V buck converter are used. To simplify the wiring to the motor controller, a hex inverter is used. All of these parts can be found below. An XBOX controller is used to be able to drive the robot.

#### Parts Needed
- [550 DC Motor](https://www.amazon.com/dp/B07D72GWPY?psc=1&ref=ppx_yo2ov_dt_b_product_details)

![550DCMotor](https://user-images.githubusercontent.com/31022165/165830312-82d7a8a6-4b9a-4e85-b55d-260aab8546b8.png)
- [BTS7960 DC Motor Driver](https://www.amazon.com/dp/B07TFB22H5?psc=1&ref=ppx_yo2ov_dt_b_product_details)

![BTS7960MotorDriver](https://user-images.githubusercontent.com/31022165/165830329-42951df0-0ffc-47e5-a5ba-0527bd04ec44.png)
- [Nema 17 Stepper Motor](https://www.amazon.com/dp/B094CQ4DBQ?ref=ppx_yo2ov_dt_b_product_details&th=1)

![StepperMotor](https://user-images.githubusercontent.com/31022165/165830411-a6c47e52-33ca-4adc-b5e4-d2917f7f05ab.png)
- [DRV8825 Stepper Motor Driver](https://www.amazon.com/dp/B07XF2LYC8?psc=1&ref=ppx_yo2ov_dt_b_product_details)


![drv8825](https://user-images.githubusercontent.com/31022165/165830381-615bfc99-a2fc-477a-99de-273e445aa8bf.png)

- [ESP8266](https://www.amazon.com/HiLetgo-Internet-Development-Wireless-Micropython/dp/B010O1G1ES/ref=sr_1_7_sspa?crid=27QFED0Q4LHKZ&keywords=esp8266&qid=1651219749&sprefix=esp8266%2Caps%2C168&sr=8-7-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFJTlM5UDZTMk5aMkkmZW5jcnlwdGVkSWQ9QTAzMTU1OTIyMEwxRjBHQ0xTVVY4JmVuY3J5cHRlZEFkSWQ9QTA3OTI1ODIzN0wwRlA3RjZaME9IJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1)

![ESP8266](https://user-images.githubusercontent.com/31022165/165908168-c8596b81-0cf3-40c4-af76-25cf2ee4cc86.png)
- [SN74HCT04 Hex Inverter](https://www.amazon.com/Instruments-SN74HC04N-CD74HC04-74HC04-Inverters/dp/B00BZQ60HU)

![HexInverter](https://user-images.githubusercontent.com/31022165/165831218-43386bf9-26d8-492d-a8cc-62805fd2dce7.png)
- [5V Buck Regulator](https://www.amazon.com/dp/B076H3XHXP?ref=ppx_yo2ov_dt_b_product_details&th=1)

![5VBuckRegulator](https://user-images.githubusercontent.com/31022165/165830424-0c7cc645-b29a-4775-be81-7ad3fa762e20.png)
- [3S Lipo Battery](https://www.amazon.com/dp/B07JQ6NGN3?psc=1&ref=ppx_yo2ov_dt_b_product_details)

![3SLipo](https://user-images.githubusercontent.com/31022165/165830442-d7d18ca3-a3fe-44bd-b53c-76f909893ea5.png)
- [XBOX Controller](https://www.amazon.com/dp/B07ZGD53JF?ref=ppx_yo2ov_dt_b_product_details&th=1)

![XBOX Controller](https://user-images.githubusercontent.com/31022165/165830449-8c5ee50a-73a9-4d0b-8959-d7919f0819ed.png)

#### Schematic
Below is a wiring diagram of how to make all of the connections needed for this project to work.

###### Wiring Diagram
![Swerve Wiring Diagram drawio](https://user-images.githubusercontent.com/31022165/165910399-0550e362-3d2a-4f34-8dc4-c8ed60317354.png)

## Software Design
The software to control the swerve drive robot is made up of two parts. First, there is a python script that takes controller inputs from the XBOX controller and converts the data to be sent over Wi-Fi to the ESP8266 connected to the MBED. Secondly, the MBED reads the incoming data over a serial port and does the math to convert joystick inputs into wheel positions and speeds. The inverse kinematics math that needs to be performed can be found from [this whitepaper](https://www.chiefdelphi.com/t/paper-4-wheel-independent-drive-independent-steering-swerve/107383). Once the appropriate wheel positions and speeds are calculated, those commands can be sent out to the appropriate motor drivers and stepper motor drivers. Custom libraries for these motor drivers were designed to be able to accept these specific inputs.

###### High Level Software Flow
![high_level_software_overview](https://user-images.githubusercontent.com/57779689/165907811-20b8924f-50be-4dae-a48a-8eff7c0bc9cd.png)

###### Swerve Drive Inverse Kinematics
![SwerveInverseKinematics](https://user-images.githubusercontent.com/31022165/165910603-000973e4-2409-4e3d-ab2b-fc209b10513f.png)



#### ESP8266 Software
All of the ESP8266 software used for this project can be found at the link below.
- https://github.com/Ahellrigel33/MiniSwerveDrive/tree/master/esp8266_setup

The ESP8266 should be flashed using Arduino IDE. Follow [these instructions](http://arduino.esp8266.com/Arduino/versions/2.0.0/doc/installing.html) to download the library to use ESP8266 through the Arduino IDE. 

In the esp8266_setup.ino file, replace the network name/password strings with the network that your computer will be connected to.

#### MBed Software
All of the mbed software used for this project can be found at the link below.
- https://os.mbed.com/users/andrewh33/code/SwerveDriveRobot/


#### Python Software
All of the python software used for this project can be found at the link below.
- https://github.com/Ahellrigel33/MiniSwerveDrive/blob/master/swerve_drive_controller.py

In the python code, replace the existing IP address for ESP8266 with the IP address outputted by the ESP8266 on the Arduino Serial Monitor.

