# using the Python GPIO Library
#https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

import RPi.GPIO as GPIO

#There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. 
#The first is using the BOARD numbering system. This refers to the pin numbers on the P1 header of the Raspberry Pi board. 
GPIO.setmode(GPIO.BOARD)

GPIO.output(38,1)