from machine import Pin, UART
import time

led=Pin(25,Pin.OUT)

# Configure UART1 with a baud rate of 9600
uart1 = UART(1, baudrate=9600, tx=4, rx=5)  # TX on Pin 4, RX on Pin 5

while True:
    #send message
    uart1.write(input())
