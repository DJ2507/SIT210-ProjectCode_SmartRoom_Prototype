# SIT210 - Project - Smart Room - Prototype
## Student
* Devin Jayasinghe

## Overview
The embedded system created for this SIT210 project is a system that would handle the sensing and analysis of temperature and humidity in a room to control smart plugs for 3 devices (represented by 3 different LEDs in the prototype) to turn the heater, humidifier and light on/off based on set target vales for the temperature and humidity in addition to using a motion sensor to check if I was in the room or not to decided whether they should continue operating or not. Furthermore, when all devices are switched off, using IFTT Webhooks the user would be notified using email and mobile notifications.

## Hardware Required
* Raspberry Pi 2B
* Adafruit DHT22 Temperature & Humidity Sensor
* HC-SR501 PIR Infrared Motion Sensor
* Breadboard
* Minimum 12 M/F Jumper Wires
* 3 LEDs (Blue, Green and Red)

## Software Required
* Python3
* IDE
* Web Browser (IFTTT & Webhooks)

### Software Dependencies 
* requests library
  ```console
  foo@bar:~$ sudo pip3 install requests
  ```
* Adafruit_DHT library
  ```console
  foo@bar:~$ sudo pip3 install Adafruit_DHT
  ```
* RPi.GPIO library (Should already be included on RPi)
  ```console
  foo@bar:~$ sudo pip3 install RPi.GPIO
  ```
* tkinter library (Should already be included in Python3)
  * Website: https://tkdocs.com/tutorial/install.html#installlinux
* time library (Should already be included in Python3)
