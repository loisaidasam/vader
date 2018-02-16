# vader

# Raspberry Pi Basic Setup

## Erase SD Card

Put blank SD card into computer. Use Disk Utility (OSX) to erase the image using format `MS-DOS (FAT)` and name it something. I'm calling mine `"VADER"`, obviously.

![screen shot 2018-02-15 at 9 04 19 pm](https://user-images.githubusercontent.com/213281/36290596-0dc4f43a-1294-11e8-8c23-4990b972201d.png)

Nice reference if you run into Disk Utility trouble: https://www.michaelcrump.net/the-magical-command-to-get-sdcard-formatted-for-fat32/

## Put the software onto the pi

Download `Raspbian Stretch Lite` from https://www.raspberrypi.org/downloads/raspbian/ and unzip it.

Use Etcher (https://etcher.io/) to burn the image onto your SD card. The image I'm using is `2017-11-29-raspbian-stretch-lite.img`.

![screen shot 2018-02-15 at 9 32 03 pm](https://user-images.githubusercontent.com/213281/36291839-94ec0604-129b-11e8-8ac8-c59c27632a3a.png)

Alternatively, download [NOOBS](https://www.raspberrypi.org/downloads/noobs/) (`New Out Of the Box Software`) and go that way.

## Get the pi running and updated

If the keyboard is weird (maybe typing `"` results in a `@`), try this: https://elinux.org/R-Pi_Troubleshooting#Re-mapping_the_keyboard_with_Debian_Squeeze

Set up wifi: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis

First off do:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```
