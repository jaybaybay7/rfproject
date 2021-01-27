#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio

GPIO.setmode(GPIO.BOARD)

pi = pigpio.pi()
rx = piVirtualWire.rx(pi,2,1000)
GPIO.setup(13,GPIO.IN)

msg = "hi"

print ("hi")

while True:
    # print (rx.ready())
    while rx.ready():
        print(rx.get())

time.sleep(0.5)

if msgGet == msg:

    GPIO.output(25,1)


rx.cancel()
pi.stop()
