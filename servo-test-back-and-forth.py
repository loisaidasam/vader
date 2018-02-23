# Servo Control
# via https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor?view=all

import time
import wiringpi

#MIN = 50
#MIN = 100
MIN = 75
#MAX = 250
#MAX = 200
MAX = 225

#DELAY_PERIOD = 0.01
DELAY_PERIOD = 0.005

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

while True:
        for pulse in range(MIN, MAX, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(DELAY_PERIOD)
        for pulse in range(MAX, MIN, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(DELAY_PERIOD)

