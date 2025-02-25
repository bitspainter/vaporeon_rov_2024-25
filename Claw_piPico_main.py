from machine import Pin, PWM
import time

# Stepper motor pins for first stepper
DIR_PIN1 = Pin(15, Pin.OUT)
STEP_PIN1 = Pin(14, Pin.OUT)

# Stepper motor pins for second stepper
DIR_PIN2 = Pin(13, Pin.OUT)  
STEP_PIN2 = Pin(12, Pin.OUT)  

# Servo pins
SERVO1_PIN = Pin(10)
SERVO2_PIN = Pin(11)

# Create PWM instances for both servos
servo1 = PWM(SERVO1_PIN, freq=50)
servo2 = PWM(SERVO2_PIN, freq=50)

def turn_servo(servo, angle):
    duty = int(angle / 180 * 10000)  
    servo.duty_u16(duty)

def turn_stepper(steps, direction, stepper_number):
    if stepper_number == 1:
        DIR_PIN1.value(direction)
        for i in range(steps):
            STEP_PIN1.value(1)
            time.sleep(0.001)
            STEP_PIN1.value(0)
            time.sleep(0.001)
    elif stepper_number == 2:
        DIR_PIN2.value(direction)
        for i in range(steps):
            STEP_PIN2.value(1)
            time.sleep(0.001)
            STEP_PIN2.value(0)
            time.sleep(0.001)

# Initial angles for both servos
angle1 = 90
angle2 = 90

while True:
    # Move both servos to their respective angles
    turn_servo(servo1, angle1)
    turn_servo(servo2, angle2)

    command = input("Enter command: ").strip().lower()

    if command == "d":
        turn_stepper(30, 1, 1)  # First stepper forward
        time.sleep(0.001)

    elif command == "a":
        turn_stepper(30, 0, 1)  # First stepper backward
        time.sleep(0.001)

    elif command == "q":
        turn_stepper(30, 1, 2)  # Second stepper forward
        time.sleep(0.001)

    elif command == "e":
        turn_stepper(30, 0, 2)  # Second stepper backward
        time.sleep(0.001)

    elif command == "t":
        angle1 += 10
        if angle1 > 150:
            angle1 = 150

    elif command == "y":
        angle1 -= 10
        if angle1 < 30:
            angle1 = 30

    elif command == "u":  # New command for servo2
        angle2 += 10
        if angle2 > 150:
            angle2 = 150

    elif command == "i":  # New command for servo2
        angle2 -= 10
        if angle2 < 30:
            angle2 = 30

    elif command == "r":
        angle1 = 90
        angle2 = 90  # Reset both servos to 90 degrees
