#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio

pi = pigpio.pi()
rx = piVirtualWire.rx(pi,2,1000)


while True:
   while rx.ready():
        msgGet = rx.get()
        print(msgGet)

time.sleep(0.5)

if msgGet = msg:
    GPIO.output(25,1)


rx.cancel()
pi.stop()