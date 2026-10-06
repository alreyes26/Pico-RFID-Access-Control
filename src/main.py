from machine import Pin, UART
import time


uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

