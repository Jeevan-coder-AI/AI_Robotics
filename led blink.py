from gpiozero import LED
from time import sleep
led=LED(23)
while True:
    led.on()
    sleep(2)
    led.off()
    sleep(2)
    






