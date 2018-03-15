#!/usr/bin/env python

import datetime
import os
import time

import RPi.GPIO as GPIO

PIN_READ = 23

GPIO.setmode(GPIO.BCM)

# Button to GPIO23
GPIO.setup(PIN_READ, GPIO.IN, pull_up_down=GPIO.PUD_UP)

command_sound = "/home/sam/source/vader/play-random-sound.sh &"

#command = "sudo python /home/sam/source/vader/servo-one-cycle.py"
command = "python /home/sam/source/vader/servo-one-cycle-pigpio.py"

try:
    while True:
        button_state = GPIO.input(23)
        if not button_state:
            # print "%s\tButton pressed..." % datetime.datetime.now()
            os.system(command_sound)
            os.system(command)
        time.sleep(0.2)
except Exception as exception:
    print exception
finally:
    GPIO.cleanup()

