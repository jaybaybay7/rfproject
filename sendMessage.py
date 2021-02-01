mport piVirtualWire.piVirtualWire as piVirtualWire
import RPi.GPIO as GPIO
import pigpio
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
                 

print('running')
state = True

counter = 0

while counter < 10:
    print(state)
    GPIO.output(37, state)
    counter = counter  + 1
    if counter == 9:
        state = not state
        counter = 0

GPIO.cleanup()