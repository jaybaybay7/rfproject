from rpi_rf import RFDevice
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)

rfdevice = RFDevice(args.gpio)

while True:
    if str(rfdevice.rx_code) == str(345):
        GPIO.output(40,1)
