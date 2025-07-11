from gpiozero import LEDBoard
from time import sleep
from signal import pause
led=LEDBoard(2,3,4,17,27,22,14)
inputs = input("Enter 7 inputs (space separated): ").split()
while True:
    # Turn on all LEDs in sequence
    for i in range(0,7):

        led.value = [int(x) for x in inputs]
        sleep(0.5)