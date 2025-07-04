from gpiozero import DigitalInputDevice,LED
from time import sleep
led=LED(14)  # GPIO pin for the LED
ir=DigitalInputDevice(17)  # GPIO pin for the IR sensor
while True:
    if ir.value:
        print("Obstacle detected!")
        led.on()
    else:
        print("No obstacle detected.") 
        led.off()
    print(ir.value)
    sleep(0.1)