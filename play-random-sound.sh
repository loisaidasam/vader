#!/bin/bash

sounds_dir="/home/sam/source/vader/sounds"

filename=$(ls $sounds_dir | sort -R  | head -n 1)

filename="$sounds_dir/$filename"

sudo aplay -q $filename

