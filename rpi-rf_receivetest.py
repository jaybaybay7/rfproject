#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
import RPi.GPIO as GPIO

from rpi_rf import RFDevice

GPIO.setmode(GPIO.BCM)

GPIO.setup(20,GPIO.OUT)
GPIO.output(20,0)

rfdevice = None

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))
while True:
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        logging.info(str(rfdevice.rx_code) +
                     " [pulselength " + str(rfdevice.rx_pulselength) +
                     ", protocol " + str(rfdevice.rx_proto) + "]")
        print(str(rfdevice.rx_code))
        if str(rfdevice.rx_code) == str(345):
            print(str(rfdevice.rx_code))
            GPIO.output(20,1)
        if tr(rfdevice.rx_code) == str(789):
            print(str(rfdevice.rx_code))
            GPIO.output(20,0)
    time.sleep(0.01)
rfdevice.cleanup()