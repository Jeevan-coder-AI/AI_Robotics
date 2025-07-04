from gpiozero import DigitalInputDevice,DigitalOutputDevice
from time import sleep
buzz=DigitalOutputDevice(14)  # GPIO pin for the LED
ir=DigitalInputDevice(17)  # GPIO pin for the IR sensor
while True:
    if ir.value:
        print("Obstacle detected!")
        buzz.on()
    else:
        print("No obstacle detected.") 
        buzz.off()
    print(ir.value)
    sleep(0.1)