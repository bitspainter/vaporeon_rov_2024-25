
from machine import Pin, PWM
import time

# Servo pins
SERVO4_PIN = Pin(8) # main pitch
SERVO5_PIN = Pin(7) # rotation

SERVO1_PIN = Pin(9)  # secondary pitch
SERVO2_PIN = Pin(10) # roll
SERVO3_PIN = Pin(11) # clamp

#PWM instances
servo1 = PWM(SERVO1_PIN, freq=50)
servo2 = PWM(SERVO2_PIN, freq=50)
servo3 = PWM(SERVO3_PIN, freq=50)
servo4 = PWM(SERVO4_PIN, freq=50)
servo5 = PWM(SERVO5_PIN, freq=50)

#delay
delay = 0.001

def turn_servo(servo, angle):
    duty = int(angle / 180 * 10000)  
    servo.duty_u16(duty)

# Initial servo angles 
angle1 = angle2 = angle3 = angle4 = angle5 = 90

while True:
    
    # always turn servos to anglex
    turn_servo(servo1, angle1)
    turn_servo(servo2, angle2)
    turn_servo(servo3, angle3)
    turn_servo(servo4, angle4)
    turn_servo(servo5, angle5)
    
    command = input("Enter command: ").strip().lower()

    #reset
    if command == "r":
        angle1 = angle2 = angle3 = angle4 = angle5 = 90
        
    # secondary pitch
    if command == "e":
        angle1 += 10
        if angle1 > 150:
            angle1 = 150

    elif command == "q":
        angle1 -= 10
        if angle1 < 30:
            angle1 = 30

    # roll
    elif command == "x":  
        angle2 += 10
        if angle2 > 150:
            angle2 = 150

    elif command == "z":  
        angle2 -= 10
        if angle2 < 30:
            angle2 = 30
    
    # clamp
    elif command == "c":  
        angle3 += 60
        if angle3 > 150:
            angle3 = 150

    elif command == "v":  
        angle3 -= 60
        
        if angle3 < 30:
            angle3 = 30

    # main pitch
    elif command == "w":  
        angle4 += 10
        if angle4 > 150:
            angle4 = 150

    elif command == "s":  
        angle4 -= 10
        if angle4 < 30:
            angle4 = 30          
  
    # rotation
    elif command == "a":  
        angle5 += 10
        if angle5 > 150:
            angle5 = 150
            
    elif command == "d":  
        angle5 -= 10
        if angle5 < 30:
            angle5 = 30

