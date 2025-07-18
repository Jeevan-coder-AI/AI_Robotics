from gpiozero import Motor
from time import sleep

motor=Motor(23,24)

try:
    while True:
        motor.forward()
        sleep(3)
        motor.stop()
        sleep(2)
        motor.backward()
        sleep(3)
        motor.stop()
        sleep(2)

except KeyboardInterrupt:
    motor.close()
            