from gpiozero import Button,LED
from signal import pause    
from time import sleep
led=LED(17)  # GPIO pin for the LED
button=Button(2)


button.when_pressed = led.on
button.when_released = led.off  
pause()  # Keep the script running to listen for button events