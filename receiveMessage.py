#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio
import time

GPIO.setmode(GPIO.BOARD)

pi = pigpio.pi()
rx = piVirtualWire.rx(pi,2,2000)
GPIO.setup(13,GPIO.IN)

msg = "hi"

while True:
    while rx.ready():
        print(rx.ready())
        msgGet = rx.get()
        print(rx.get())

 time.sleep(0.5)
 
# if msgGet == msg:
#     GPIO.output(25,1)

rx.cancel()
pi.stop()
ssh
# print ("hi")

# while True:
#     state = GPIO.input(13)
#     print(state)
#     time.sleep(0.1)

# GPIO.cleanup()
