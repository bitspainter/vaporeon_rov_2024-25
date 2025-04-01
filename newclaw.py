from machine import Pin, PWM
import time

# Servo pins
SERVO4_PIN = Pin(8)  # main pitch
SERVO5_PIN = Pin(7)  # rotation

SERVO1_PIN = Pin(9)  # secondary pitch
SERVO2_PIN = Pin(10) # roll
SERVO3_PIN = Pin(11) # clamp

# New servos
SERVO6_PIN = Pin(12) # new servo 1
SERVO7_PIN = Pin(13) # new servo 2
SERVO8_PIN = Pin(14) # new servo 3
SERVO9_PIN = Pin(15) # new servo 4
SERVO10_PIN = Pin(16) # new servo 5

# PWM instances
servo1 = PWM(SERVO1_PIN, freq=50)
servo2 = PWM(SERVO2_PIN, freq=50)
servo3 = PWM(SERVO3_PIN, freq=50)
servo4 = PWM(SERVO4_PIN, freq=50)
servo5 = PWM(SERVO5_PIN, freq=50)
servo6 = PWM(SERVO6_PIN, freq=50) # new servo 1
servo7 = PWM(SERVO7_PIN, freq=50) # new servo 2
servo8 = PWM(SERVO8_PIN, freq=50) # new servo 3
servo9 = PWM(SERVO9_PIN, freq=50) # new servo 4
servo10 = PWM(SERVO10_PIN, freq=50) # new servo 5

# Delay
delay = 0.001

def turn_servo(servo, angle):
    duty = int(angle / 180 * 10000)  
    servo.duty_u16(duty)

# Initial servo angles 
angle1 = angle2 = angle3 = angle4 = angle5 = 90
angle6 = angle7 = angle8 = angle9 = angle10 = 90 # new angles for new servos

while True:
    
    # Always turn servos to angles
    turn_servo(servo1, angle1)
    turn_servo(servo2, angle2)
    turn_servo(servo3, angle3)
    turn_servo(servo4, angle4)
    turn_servo(servo5, angle5)
    turn_servo(servo6, angle6) # new servo 1
    turn_servo(servo7, angle7) # new servo 2
    turn_servo(servo8, angle8) # new servo 3
    turn_servo(servo9, angle9) # new servo 4
    turn_servo(servo10, angle10) # new servo 5
    
    command = input("Enter command: ").strip().lower()

    # Reset
    if command == "r":
        angle1 = angle2 = angle3 = angle4 = angle5 = 90
        angle6 = angle7 = angle8 = angle9 = angle10 = 90 # reset new servos

    # Secondary pitch
    if command == "e":
        angle1 += 10
        if angle1 > 150:
            angle1 = 150

    elif command == "q":
        angle1 -= 10
        if angle1 < 30:
            angle1 = 30

    # Roll
    elif command == "x":  
        angle2 += 10
        if angle2 > 150:
            angle2 = 150

    elif command == "z":  
        angle2 -= 10
        if angle2 < 30:
            angle2 = 30
    
    # Clamp
    elif command == "c":  
        angle3 += 60
        if angle3 > 150:
            angle3 = 150

    elif command == "v":  
        angle3 -= 60
        if angle3 < 30:
            angle3 = 30

    # Main pitch
    elif command == "w":  
        angle4 += 10
        if angle4 > 150:
            angle4 = 150

    elif command == "s":  
        angle4 -= 10
        if angle4 < 30:
            angle4 = 30          
  
    # Rotation
    elif command == "a":  
        angle5 += 10
        if angle5 > 150:
            angle5 = 150
            
    elif command == "d":  
        angle5 -= 10
        if angle5 < 30:
            angle5 = 30

    # Control new servos
    # New servo 1
    elif command == "t":
        angle6 += 10
        if angle6 > 150:
            angle6 = 150
            
    elif command == "g":
        angle6 -= 10
        if angle6 < 30:
            angle6 = 30

    # New servo 2
    elif command == "y":
        angle7 += 10
        if angle7 > 150:
            angle7 = 150
            
    elif command == "h":
        angle7 -= 10
        if angle7 < 30:
            angle7 = 30

    # New servo 3
    elif command == "u":
        angle8 += 10
        if angle8 > 150:
            angle8 = 150
            
    elif command == "j":
        angle8 -= 10
        if angle8 < 30:
            angle8 = 30

    # New servo 4
    elif command == "i":
        angle9 += 10
        if angle9 > 150:
            angle9 = 150
            
    elif command == "k":
        angle9 -= 10
        if angle9 < 30:
            angle9 = 30

    # New servo 5
    elif command == "o":
        angle10 += 10
        if angle10 > 150:
            angle10 = 150
            
    elif command == "l":
        angle10 -= 10
        if angle10 < 30:
            angle10 = 30
