import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)
GPIO.setup(13, GPIO.IN)

msg = 12345

if GPIO.input(13) == msg:
    GPIO.output(40,1)

