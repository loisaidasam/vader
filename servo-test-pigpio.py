#!/usr/bin/env python

# via https://raspberrypiwonderland.wordpress.com/2014/02/19/servo-test/

import time

import pigpio

# GPIO number
PIN = 18

pi = pigpio.pi()
# pulsewidth can only set between 500-2500

try:
    pi.set_mode(PIN, pigpio.OUTPUT)
    pi.set_servo_pulsewidth(PIN, 1500)
    time.sleep(5)
    pi.set_servo_pulsewidth(PIN, 1000)
    time.sleep(5)
    pi.set_servo_pulsewidth(PIN, 1500)
    time.sleep(5)
    #pi.set_servo_pulsewidth(PIN, 0)
finally:
    pi.stop()


'''
try:
    while True:
        # 0 degree
        pi.set_servo_pulsewidth(servos, 500)
        print("Servo {} {} micro pulses".format(servos, 1000))
        time.sleep(1)
        # 90 degree
        pigpio.set_servo_pulsewidth(servos, 1500)
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
        # 180 degree
        pigpio.set_servo_pulsewidth(servos, 2500)
        print("Servo {} {} micro pulses".format(servos, 2000))
        time.sleep(1)
        # 180 degree
        pigpio.set_servo_pulsewidth(servos, 1500)
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)

# switch all servos off
except KeyboardInterrupt:
    pigpio.set_servo_pulsewidth(servos, 0)

pigpio.stop()
'''
