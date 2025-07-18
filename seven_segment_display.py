from gpiozero import LEDCharDisplay
from time import sleep

display=LEDCharDisplay(22,27,17,4,3,2,14)

try:
    while True:
        for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            try:
                display.value=i
            
            except KeyError:
                print(f"The character \"{i}\" cannot be displayed.")
            
            sleep(0.5)

except KeyboardInterrupt:
    display.close()