from gpiozero import LED
from time import sleep

led=LED(14)

try:
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

except KeyboardInterrupt:
    led.close()