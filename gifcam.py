import picamera
from time import sleep
import time
import RPi.GPIO as GPIO
from os import system
import os
import random, string
import shutil
# from twython import Twython

########################
#
# Behaviour Variables
#
########################
num_frame = 8       # Number of frames in Gif
########################
#
# Define GPIO
#
########################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 19 #Button GPIO Pin
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_1 = 12 #Status LED GPIO Pin
GPIO.setup(led_1, GPIO.OUT)
buttonLed = GPIO.PWM(led_1, 10)
led_2 = 21 #ON/OFF LED Pin
GPIO.setup(led_2, GPIO.OUT)
statusLed = GPIO.PWM(led_2, 2)


########################
#
# Camera
#
########################
camera = picamera.PiCamera()
camera.resolution = (540, 405)
camera.rotation = 90
#camera.brightness = 70
camera.image_effect = 'none'
##GPIO.output(led_2, 1)
camera.start_preview()
time.sleep(2)

# Indicate ready status
buttonLed.start(100)
statusLed.start(0)

print('System Ready')

try:
    while True:
        if GPIO.input(button) == False: # Button Pressed
            ### TAKING PICTURES ###
            print('Gif Started')
            statusLed.ChangeDutyCycle(0)
            buttonLed.ChangeDutyCycle(50)

            name = time.strftime('%Y%m%d%H%M%S')
            camera.start_recording('tmp/%s.h264' %(name))
            camera.wait_recording(3)
            camera.stop_recording()
            os.system("mv ./tmp/" + name + ".h264 ./raw/" + name) # cleanup source images
            print('Done')
            buttonLed.ChangeDutyCycle(0)

        else : # Button NOT pressed
            ### READY TO MAKE GIF ###
            statusLed.ChangeDutyCycle(0)
            buttonLed.ChangeDutyCycle(100)
            sleep(0.05)

except Exception,e:
    print str(e)
    GPIO.cleanup()
