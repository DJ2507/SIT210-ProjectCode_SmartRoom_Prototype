# Imports Required Libraries
import RPi.GPIO as GPIO
import time
import requests
from tkinter import *
import Adafruit_DHT

# Sets Pin Numbers For Each Variable
pir_sensor = 11
lightled = 36
templed = 38
humled = 40
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Sets GPIO Board UP & Sets Pins As Input or Output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(humled, GPIO.OUT)
GPIO.setup(templed, GPIO.OUT)
GPIO.setup(lightled, GPIO.OUT)   

# Code For Decisions
def smartroom_code(settemperature, sethumidity):
    timer = 0 # Sets Timer
    current_state = 0 # Sets Current State
    time.sleep(0.1)
    current_state = GPIO.input(pir_sensor) # Checks For Motion (1=Motion & 0=No Motion)

    # Sets Timer Value Based on Motion Detected
    if current_state == 1: # If Motion is Detected Set Timer To 0 (0mins)
        timer = 0
    if current_state == 0: # If No Motion is Detected Add 1 (5sec) To Timer
        timer += 1
    if timer >= 60: # If Timer is >= 60 Set Timer To 60 (Conserves Memory)
        timer = 60

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) # Read Humidity & Temperature From Sensor & Set To Variables
    
    # If Timer < 60 (Motion Detected Within 5mins)
    if timer < 60:
        if humidity < (sethumidity - 3): # If Humidity < Acceptable Range of Target Humidity Switch On Humidifier
            GPIO.output(humled, True)
        else: GPIO.output(humled, False) # If Not Switch Off Humidifier
        if temperature < (settemperature - 2): # If Temperature < Acceptable Range of Target Temperature Switch On Heater
            GPIO.output(templed, True) 
        else: GPIO.output(templed, False) # If Not Switch Off Heater
        GPIO.output(lightled, True) # Switch On Light 
        
    # If Timer > 60 (No Motion For 5mins)
    if timer > 60:
        GPIO.output(humled, False) # Turn Humidifier Off
        GPIO.output(templed, False) # Turn Heater Off
        GPIO.output(lightled, False) # Turn Light Off
        r = requests.post('https://maker.ifttt.com/trigger/all_off/with/key/nZhqWJolBYnxYQztknC5P') # Post Event Trigger (Causes IFTTT Webhook To Send Email + Mobile Notification 
                                                                                                    # Saying Devices Have Been Switched Off)
    time.sleep(5) # Wait 5 Seconds

# Function To Run Main Program
def run_room():
    while True:
        settemperature = int(textInput1.get()) # Gets Target Temperature
        sethumidity = int(textInput2.get()) # Gets Target Humidity
        smartroom_code(settemperature, sethumidity)

# Function For Switching Off LEDs, Cleaning GPIO & Closing Window
def close():
    GPIO.output(humled, False)
    GPIO.output(templed, False)
    GPIO.output(lightled, False)
    RPi.GPIO.cleanup()
    win.destroy()

# Creates Window
win = Tk()
win.title("Paramters")

# Creates Window For Entering Target Values
# Entry Box 1 & Location For Temperature
textInput1 = Entry(win, bg='bisque2')
textInput1.grid(row=0,column=1

# Entry Box 2 & Location (For Humidity)
textInput2 = Entry(win, bg='bisque2')
textInput2.grid(row=1,column=1)

# Labels
Label(win, text="Temperature").grid(row=0,column=0)
Label(win, text="Humidity").grid(row=1,column=0)

# Enter/Begin Button
ledButton = Button(win, text='Enter', command=run_room, bg='bisque2', height=1, width=17)
ledButton.grid(row=3,column=1)

# Exit Button
exitButton = Button(win, text='Exit', command=close, bg='red', height=1, width=6)
exitButton.grid(row=4, column=1)

win.protocol("WM_DELETE_WINDOW", close) # When Window Closed Run Close Function

win.mainloop()
