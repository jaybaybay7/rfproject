#!/usr/bin/env python

import piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio

GPIO.setmode(GPIO.BOARD)

pi = pigpio.pi()
rx = piVirtualWire.rx(pi,2,1000)
GPIO.setup(37,GPIO.OUT)

msg = "hi"

print ("hi")

while True:
    print("hello")
    print (rx.ready())
    while rx.ready():
        print("hola")
        print(rx.get())

print("forth")
time.sleep(0.5)


if msgGet == msg:

    GPIO.output(37,1)


rx.cancel()
pi.stop()
