from machine import Pin
import time

DIR_PIN = Pin(15, Pin.OUT)
STEP_PIN = Pin(14, Pin.OUT)
speed = 1

def turn_stepper (steps, direction):
    
    DIR_PIN.value(direction)
    
    for i in range (steps):
        STEP_PIN.value(1)
        time.sleep(0.001)
        STEP_PIN.value(0)
        time.sleep(0.001)
        
while True:
    
    command = input("enter: d = >, a = <, e = sp.up, q = sp.down: ", ).strip().lower()
    
    if command == "e":
        
        speed += 1

    elif command == "q":
        
        speed -= 1
        if speed == 0:
            speed = 1
        
    elif command == "d":
    
        turn_stepper(10*speed,1)
        time.sleep(0.001)
    
    elif command == "a":
        
        turn_stepper(10*speed,0)
        time.sleep(0.001)
    
    
