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

# Indicate ready status
buttonLed.start(100)
statusLed.start(0)

print('System Ready')

try:
    while True:
        if GPIO.input(button) == False: # Button Pressed
        
            print("button")
            ### TAKING PICTURES ###
            print('Gif Started')
            statusLed.ChangeDutyCycle(0)
            buttonLed.ChangeDutyCycle(50)

            randomstring = time.strftime('%Y%m%d%H%M%S')
            tmp = 'tmp/%s' %(randomstring)
            raw = 'raw/%s' %(randomstring)
            os.makedirs(tmp)
            for i in range(num_frame):
                number = '{0:04d}'.format(i)
                camera.capture('tmp/%s/%s.jpg' %(randomstring, number))

            shutil.move(tmp, raw)
            print('Done')
            print('System Ready')

            buttonLed.ChangeDutyCycle(0)

        else : # Button NOT pressed
            ### READY TO MAKE GIF ###
            statusLed.ChangeDutyCycle(0)
            buttonLed.ChangeDutyCycle(100)
            sleep(0.05)

except Exception,e:
    print str(e)
    GPIO.cleanup()
