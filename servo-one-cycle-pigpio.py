#!/usr/bin/env python

"""
The selected pulsewidth will continue to be transmitted until changed by a
subsequent call to set_servo_pulsewidth.

The pulsewidths supported by servos varies and should probably be determined by
experiment. A value of 1500 should always be safe and represents the mid-point
of rotation.

You can DAMAGE a servo if you command it to move beyond its limits.

Example

pi.set_servo_pulsewidth(17, 0)    # off
pi.set_servo_pulsewidth(17, 1000) # safe anti-clockwise
pi.set_servo_pulsewidth(17, 1500) # centre
pi.set_servo_pulsewidth(17, 2000) # safe clockwise

https://raspberrypiwonderland.wordpress.com/2014/02/19/servo-test/
http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth
http://abyz.me.uk/rpi/pigpio/index.html
https://elinux.org/RPi_GPIO_Code_Samples#pigpio_2
"""

import time

import pigpio

# GPIO number
PIN = 18

# Safe
#MIN = 1000
#MAX = 2000

# Too much
#MIN = 500
#MAX = 2500

# Going with
MIN = 850
MAX = 2150

STEP = 2

DELAY = 0.00005
#DELAY = 0

pi = pigpio.pi()
# pulsewidth can only set between 500-2500

try:
    pi.set_mode(PIN, pigpio.OUTPUT)
    for pulse in range(MAX, MIN, -1 * STEP):
        print pulse
        pi.set_servo_pulsewidth(PIN, pulse)
        time.sleep(DELAY)
    for pulse in range(MIN, MAX, STEP):
        print pulse
        pi.set_servo_pulsewidth(PIN, pulse)
        time.sleep(DELAY)
except KeyboardInterrupt:
    print "Caught KeyboardInterrupt"
    pi.set_servo_pulsewidth(PIN, 0)
finally:
    print "Stopping"
    pi.stop()
    print "Done"

