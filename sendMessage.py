# using the Python GPIO Library
#https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio


#There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. 
#The first is using the BOARD numbering system. This refers to the pin numbers on the P1 header of the Raspberry Pi board. 
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(37,GPIO.OUT)


pi = pigpio.pi()
tx = piVirtualWire.tx(pi,27,1000)

msg = "100"

tx.put(msg)
tx.waitForReady()

tx.cancel()
pi.stop()

while True:
   while rx.ready():
        msgGet = rx.get()
        print(msgGet)

    time.sleep(0.5)

if msgGet = msg:
    GPIO.output(25,1)


tx.cancel()
rx.cancel()

pi.stop()








#GPIO.setup(38,GPIO.OUT)
#GPIO.output(38,1)