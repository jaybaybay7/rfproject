# https://pypi.org/project/raspi-lora/

from raspi-lora import LoRa, ModemConfig

def onReceived(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)



#initialization step
"""
LoRa(channel, interrupt, this_address, freq=915, tx_power=14,
      modem_config=ModemConfig.Bw125Cr45Sf128, acks=False, crypto=None)
channel SPI channel to use (either 0 or 1, if your LoRa radio is connected to CE0 or CE1, respectively)

interrupt GPIO pin (BCM-style numbering) to use for the interrupt

this_address The address number (0-254) your device will use when sending and receiving packets.

freq Frequency used by your LoRa radio. Defaults to 915Mhz

tx_power Transmission power level from 5 to 23. Keep this as low as possible. Defaults to 14

model_config Modem configuration. See RadioHead docs. Default to Bw125Cr45Sf128.

receive_all Receive messages regardless of the destination address

acks If True, send an acknowledgment packet when a message is received and wait for an acknowledgment when transmitting a message. This is equivalent to using RadioHead's RHReliableDatagram

crypto An instance of PyCryptodome Cipher.AES (see above example)"
"""

# Use chip select 0. GPIO pin 17 will be used for interrupts
# The address of this device will be set to 2

lora = LoRa(0, 17, 2, freq=433, modem_config=ModemConfig.Bw125Cr45Sf128, tx_power=14, acks=True)

lora.onReceived = onReceived

#initialization step - Done

#set mode to always transmit
lora.set_mode_rx()






lora.close()