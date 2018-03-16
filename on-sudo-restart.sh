#!/bin/bash

# Start pigpiod
/usr/bin/pigpiod 

# Set the volume
#/home/sam/source/vader/bin_home/volume_default.sh

# Play a welcome sound
/usr/bin/aplay /home/sam/source/vader/sounds/proud.wav

# Kick it off
python /home/sam/source/vader/vader.py > /home/sam/source/vader/logs/vader.log 2>&1

