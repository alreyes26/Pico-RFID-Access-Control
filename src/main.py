from machine import Pin, UART
import time


uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

while True:
    if uart.any():
        data = uart.read()
        print(data)
    time.sleep(0.1)
    
    