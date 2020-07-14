#!/usr/bin/env python3
#-- coding: utf-8 --

# Loading Libraries
import RPi.GPIO as GPIO #Import to control GPIOs
import picamera
import datetime
import time
GPIO.setmode(GPIO.BCM) # Defining numerating mode (Board)
GPIO.setwarnings(False) # Hiding warnings messages

LED = 3 # GPIO port for the LED
BUTTON = 14 # GPIO port for the push-down button

GPIO.setup(LED, GPIO.OUT) # Enabling GPIO control
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23

state = # Reading the current state of the GPIO, True if the led is on, False otherwise
def take_picture():
    print("Taking picture...")
    with picamera.PiCamera() as camera:
        GPIO.output(LED, GPIO.HIGH) #Led ON
        time.sleep(1)
        camera.resolution = (800,600)
        current_time = datetime.datetime.now()
        # Saving image name as the current date and time.
        image_name = "/home/pi/Desktop/data/" + str(current_time) + ".jpg"
        camera.capture(image_name)
        GPIO.output(LED, GPIO.LOW) # Led OFF
    print("Picture taken.")


while True:
     button_state = GPIO.input(14)
     if button_state == False:
         print('Button Pressed...')
         take_picture()
         time.sleep(0.2)



