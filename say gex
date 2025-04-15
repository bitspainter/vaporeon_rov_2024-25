from machine import Pin, UART, PWM
import time

uart=UART(1, baudrate=9600, tx=4, rx=5)
uart.init(bits=8, parity=None, stop=1, timeout=1000)

led=Pin(25,Pin.OUT)
halt = 15*100000 #nanoseconds

#MOTOR
motor_1 = PWM(Pin(12), freq=100, duty_ns=halt)
motor_2 = PWM(Pin(11), freq=100, duty_ns=halt)
motor_3 = PWM(Pin(13), freq=100, duty_ns=halt)

motor_4 = PWM(Pin(9), freq=100, duty_ns=halt)
motor_5 = PWM(Pin(10), freq=100, duty_ns=halt)
motor_6 = PWM(Pin(8), freq=100, duty_ns=halt)

#CLAW
servo1 = PWM(Pin(14), freq=50)
servo2 = PWM(Pin(1), freq=50)
servo3 = PWM(Pin(0), freq=50)
servo4 = PWM(Pin(21), freq=50)
servo5 = PWM(Pin(20), freq=50)

servo6 = PWM(Pin(15), freq=50) # new servo 1
servo7 = PWM(Pin(6), freq=50) # new servo 2
servo8 = PWM(Pin(2), freq=50) # new servo 3
servo9 = PWM(Pin(3), freq=50) # new servo 4
servo10 = PWM(Pin(7), freq=50) # new servo 5

def brake():
    motor_1.init(freq=100, duty_ns=halt)
    motor_2.init(freq=100, duty_ns=halt)
    motor_3.init(freq=100, duty_ns=halt)
    motor_4.init(freq=100, duty_ns=halt)
    motor_5.init(freq=100, duty_ns=halt)
    motor_6.init(freq=100, duty_ns=halt)
    
def move(motor, v):
    if v <= 5 and v >= -5:
        motor.init(freq=100, duty_ns=((15+v)*100000)) #nanoseconds

def smash():
    motor_1.init(freq=100, duty_ns=1900000)
    motor_2.init(freq=100, duty_ns=1900000)
    motor_3.init(freq=100, duty_ns=1900000)
    motor_4.init(freq=100, duty_ns=1900000)
    motor_5.init(freq=100, duty_ns=1900000)
    motor_6.init(freq=100, duty_ns=1900000)

def turn_servo(servo, angle):
    duty = int(angle / 180 * 10000)  
    servo.duty_u16(duty)

def stop_servo(servo):
    servo.deinit()


s = 3
angleinc = 1

angle1 = 50
angle2 = 90
angle3 = 90
angle4 = 90
angle5 = 90

angle6 = 50
angle7 = 150
angle8 = 90
angle9 = 90
angle10 = 90


cmd = ''
while True:
    if uart.any():
        cmd = uart.read()
        print(cmd)
    
        
        if cmd == b' ':
            brake()
        elif cmd == b'q':
            move(motor_2, s)
            move(motor_5, -s)
        elif cmd == b'e':
            move(motor_2, -s)
            move(motor_5, s)
        elif cmd == b'w':
            move(motor_1, s)
            move(motor_3, s)
            move(motor_4, s)
            move(motor_6, s)
        elif cmd == b's':
            move(motor_1, -s)
            move(motor_3, -s)
            move(motor_4, -s)
            move(motor_6, -s)
        elif cmd == b'a':
            move(motor_1, -s)
            move(motor_3, -s)
            move(motor_4, s)
            move(motor_6, s)
        elif cmd == b'd':
            move(motor_1, s)
            move(motor_3, s)
            move(motor_4, -s)
            move(motor_6, -s)
        elif cmd == b'r':
            move(motor_2, s)
            move(motor_5, s)
        elif cmd == b'f':
            move(motor_2, -s)
            move(motor_5, -s)
        elif cmd == b'z':
            s = 1
            angleinc = 1
        elif cmd == b'x':
            s = 3
            angleinc = 5
        elif cmd == b'c':
            s = 4
            angleinc = 9


        #Claw_1
        if cmd == b'5':
            for i in range(angleinc):
                angle1 += 3
                if angle1 > 150:
                    angle1 = 150
                turn_servo(servo1, angle1)
                time.sleep(0.1)
        elif cmd == b't':
            for i in range(angleinc):
                angle1 -= 3
                if angle1 < 45:
                    angle1 = 45
                turn_servo(servo1, angle1)
                time.sleep(0.1)

        if cmd == b'6':
            for i in range(angleinc):
                angle2 += 3
                if angle2 > 150:
                    angle2 = 150
                turn_servo(servo2, angle2)
                time.sleep(0.1)
        elif cmd == b'y':
            for i in range(angleinc):
                angle2 -= 3
                if angle2 < 45:
                    angle2 = 45
                turn_servo(servo2, angle2)
                time.sleep(0.1)

        elif cmd == b'7':
            for i in range(angleinc):
                angle3 += 3
                if angle3 > 150:
                    angle3 = 150
                turn_servo(servo3, angle3)
                time.sleep(0.1)
        elif cmd == b'u':
            for i in range(angleinc):
                angle3 -= 3
                if angle3 < 30:
                    angle3 = 30
                turn_servo(servo3, angle3)
                time.sleep(0.1)
     
        elif cmd == b'8':
            for i in range(angleinc):
                angle4 += 3
                if angle4 > 150:
                    angle4 = 150
                turn_servo(servo4, angle4)
                time.sleep(0.1)
            
        elif cmd == b'i':
            for i in range(angleinc):
                angle4 -= 3
                if angle4 < 30:
                    angle4 = 30
                turn_servo(servo4, angle4)
                time.sleep(0.1)
      
        elif cmd == b'9':
            for i in range(angleinc):
                angle5 += 3
                if angle5 > 150:
                    angle5 = 150
                turn_servo(servo5, angle5)
                time.sleep(0.1)
        elif cmd == b'o':
            for i in range(angleinc):
                angle5 -= 3
                if angle5 < 30:
                    angle5 = 30
                turn_servo(servo5, angle5)
                time.sleep(0.1)
        
        
            #Claw_1
        if cmd == b'g':
            for i in range(angleinc):
                angle6 += 3
                if angle6 > 150:
                    angle6 = 150
                turn_servo(servo6, angle6)
                time.sleep(0.1)
        elif cmd == b'b':
            for i in range(angleinc):
                angle6 -= 3
                if angle6 < 45:
                    angle6 = 45
                turn_servo(servo6, angle6)
                time.sleep(0.1)
                
        if cmd == b'h':
            for i in range(angleinc):
                angle7 += 3
                if angle7 > 150:
                    angle7 = 150
                turn_servo(servo7, angle7)
                time.sleep(0.1)
        elif cmd == b'n':
            for i in range(angleinc):
                angle7 -= 3
                if angle7 < 45:
                    angle7 = 45
                turn_servo(servo7, angle7)
                time.sleep(0.1)

        elif cmd == b'j':
            for i in range(angleinc):
                angle8 += 3
                if angle8 > 150:
                    angle8 = 150
                turn_servo(servo8, angle8)
                time.sleep(0.1)
        elif cmd == b'm':
            for i in range(angleinc):
                angle8 -= 3
                if angle8 < 30:
                    angle8 = 30
                turn_servo(servo8, angle8)
                time.sleep(0.1)
     
        elif cmd == b'k':
            for i in range(angleinc):
                angle9 += 3
                if angle9 > 150:
                    angle9 = 150
                turn_servo(servo9, angle9)
                time.sleep(0.1)
        elif cmd == b',':
            for i in range(angleinc):
                angle9 -= 3
                if angle9 < 30:
                    angle9 = 30
                turn_servo(servo9, angle9)
                time.sleep(0.1)
      
        elif cmd == b'l':
            for i in range(angleinc):
                angle10 += 3
                if angle10 > 150:
                    angle10 = 150
                turn_servo(servo10, angle10)
                time.sleep(0.1)
        elif cmd == b'.':
            for i in range(angleinc):
                angle10 -= 3
                if angle10 < 30:
                    angle10 = 30
                turn_servo(servo10, angle10)
                time.sleep(0.1)


  




