from gpiozero import DigitalOutputDevice
from time import sleep
buzz=DigitalOutputDevice(14)
while True:
    buzz.on()
    sleep(0.1)
    buzz.off()               
    sleep(0.1)