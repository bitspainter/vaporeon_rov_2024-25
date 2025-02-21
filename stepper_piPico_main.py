
from machine import Pin
import time

DIR_PIN = Pin(15, Pin.OUT)
STEP_PIN = Pin(14, Pin.OUT)


def turn_stepper (steps, direction):
    
    DIR_PIN.value(direction)
    
    for i in range (steps):
        STEP_PIN.value(1)
        time.sleep(0.001)
        STEP_PIN.value(0)
        time.sleep(0.001)
        
while True:
    
    command = input("enter: d = >, a = <, (stepper) " ).strip().lower()
    
        
    elif command == "d":
    
        turn_stepper(100,1)
        time.sleep(0.001)
    
    elif command == "a":
        
        turn_stepper(100,0)
        time.sleep(0.001)
    
    

