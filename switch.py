from rpi_rf import RFDevice
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(38,GPIO.OUT)


rfdevice = RFDevice(27)

while True:
    if str(rfdevice.rx_code) == str(345):
        GPIO.output(38,1)
