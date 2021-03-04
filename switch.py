from rpi_rf import RFDevice
import RPi.GPIO as GPIO
import argparse

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
args = parser.parse_args()
rfdevice = RFDevice(args.gpio)

while True:
    if str(rfdevice.rx_code) == str(345):
        GPIO.output(40,1)
