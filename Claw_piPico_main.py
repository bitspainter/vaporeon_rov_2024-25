from machine import Pin, PWM
import time

# Stepper 1
DIR_PIN1 = Pin(15, Pin.OUT)
STEP_PIN1 = Pin(14, Pin.OUT)

# Stepper 2
DIR_PIN2 = Pin(13, Pin.OUT)  
STEP_PIN2 = Pin(12, Pin.OUT)  


# Servo pins
SERVO1_PIN = Pin(9)  # secondary pitch
SERVO2_PIN = Pin(10) # roll
SERVO3_PIN = Pin(11) # clamp

#PWM instances
servo1 = PWM(SERVO1_PIN, freq=50)
servo2 = PWM(SERVO2_PIN, freq=50)
servo3 = PWM(SERVO3_PIN, freq=50)

def turn_servo(servo, angle):
    duty = int(angle / 180 * 10000)  
    servo.duty_u16(duty)

def turn_stepper(steps, direction, stepper_number):
    
    if stepper_number == 1: # rotation
        DIR_PIN1.value(direction)
        
        for i in range(steps):
            STEP_PIN1.value(1)
            time.sleep(0.001)
            STEP_PIN1.value(0)
            time.sleep(0.001)
            
    elif stepper_number == 2: # main pitch
        DIR_PIN2.value(direction)
       
       for i in range(steps):
            STEP_PIN2.value(1)
            time.sleep(0.001)
            STEP_PIN2.value(0)
            time.sleep(0.001)

# Initial servo angles 
angle1 = 90
angle2 = 90
angle3 = 90

while True:
    
    # always turn servos to anglex
    turn_servo(servo1, angle1)
    turn_servo(servo2, angle2)
    turn_servo(servo3, angle3)

    command = input("Enter command: ").strip().lower()

    
    # secondary pitch
    if command == "q":
        angle1 += 10
        if angle1 > 150:
            angle1 = 150

    elif command == "e":
        angle1 -= 10
        if angle1 < 30:
            angle1 = 30

    # roll
    elif command == "z":  
        angle2 += 10
        if angle2 > 150:
            angle2 = 150

    elif command == "x":  
        angle2 -= 10
        if angle2 < 30:
            angle2 = 30
    
    # clamp
    elif command == "c":  
        angle3 += 10
        if angle3 > 150:
            angle3 = 150

    elif command == "v":  
        angle3 -= 10
        if angle3 < 30:
            angle3 = 30

    # rotation
    elif command == "d":
        turn_stepper(30, 1, 1)  
        time.sleep(0.001)

    elif command == "a":
        turn_stepper(30, 0, 1)  
        time.sleep(0.001)
    
    # main pitch
    elif command == "w":
        turn_stepper(30, 1, 2)  
        time.sleep(0.001)

    elif command == "s":
        turn_stepper(30, 0, 2)  
        time.sleep(0.001)

   
