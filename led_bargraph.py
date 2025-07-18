from gpiozero import LEDBarGraph

graph = LEDBarGraph(2,3,4,17,27,22,14,18)

try:
    while True:
        value=float(input())
        graph.value=value
        
except KeyboardInterrupt:
    graph.close()


