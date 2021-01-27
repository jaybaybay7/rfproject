# using the Python GPIO Library
#https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio
import time


#There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO.
#The first is using the BOARD numbering system. This refers to the pin numbers on the P1 header of the Raspberry Pi board.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

#
# pi = pigpio.pi()
# tx = piVirtualWire.tx(pi,27,1000)
#
# msg = "hi"
#
# while True:
#     tx.put(msg)
#     tx.waitForReady()
#
# tx.cancel()
# pi.stop()

print('running')
state = True

while True:
    print('state')
    GPIO.output(37, state)
    time.sleep(1)
    state = not state

GPIO.cleanup()
