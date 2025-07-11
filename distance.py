from gpiozero import DistanceSensor,LED
from time import sleep
from signal import pause
led=LED(25)  # GPIO pin for the LED
sensor=DistanceSensor(23, 24)
led.off()
while True:
    print('Distance to nearest object is', sensor.distance * 100, 'cm')
    sleep(1)
    if(sensor.distance<20):
        led.on()
        sleep(1)
    if(sensor.distance>20):
        led.off()   