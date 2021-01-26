#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio

pi = pigpio.pi()
rx = piVirtualWire.rx(pi,2,1000)
GPIO.setup(13,GPIO.IN)

msg = "hi"

while True:
   while rx.ready():
        print(rx.get())

time.sleep(0.5)

if msgGet == msg:

    GPIO.output(25,1)


rx.cancel()
pi.stop()