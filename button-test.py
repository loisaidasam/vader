# Button click
# via https://www.hackster.io/hardikrathod/push-button-with-raspberry-pi-6b6928

import datetime
import time

import RPi.GPIO as GPIO

PIN_READ = 23

GPIO.setmode(GPIO.BCM)

# Button to GPIO23
GPIO.setup(PIN_READ, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        button_state = GPIO.input(23)
        if button_state:
            print "%s\tButton not pressed..." % datetime.datetime.now()
        else:
            print "%s\tButton pressed..." % datetime.datetime.now()
        time.sleep(0.2)
except:
    GPIO.cleanup()
