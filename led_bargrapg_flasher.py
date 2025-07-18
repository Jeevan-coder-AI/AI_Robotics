from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(2,3,4,17,27,22,14,18)

try:
    while True:
        for i in range(1,9):
            graph.value=i/8
            sleep(0.5)
    
        for i in range(8,0,-1):
            graph.value=i/8
            sleep(0.5)

except KeyboardInterrupt:
    graph.close()