import sys
from time import sleep
from machine import Pin
from machine import PWM
from machine import UART

freq = 50

f1 = machine.Pin(20)
f1_pwm = PWM(f1)
f1_pwm.freq(50)
f1d = 0

f2 = machine.Pin(19)
f2_pwm = PWM(f2)
f2_pwm.freq(50)
f2d = 0

f3 = machine.Pin(18)
f3_pwm = PWM(f3)
f3_pwm.freq(50)
f3d = 0

f4 = machine.Pin(17)
f4_pwm = PWM(f4)
f4_pwm.freq(50)
f4d = 0

f5 = machine.Pin(22)
f5_pwm = PWM(f5)
f5_pwm.freq(50)
f5d = 0

f6 = machine.Pin(21)
f6_pwm = PWM(f6)
f6_pwm.freq(50)
f6d = 0

c1 = machine.Pin(8)
c1_pwm = PWM(c1)
c1_pwm.freq(50)
c1d = 0

c2 = machine.Pin(9)
c2_pwm = PWM(c2)
c2_pwm.freq(50)
c2d = 0

l = int(65025/2)
led = Pin(25,Pin.OUT)
uart1 = UART(1, baudrate=9600, tx=4, rx=5)  # TX on Pin 4, RX on Pin 5

# Function to send data
def send_data(data):
    try:
        uart1.write(data.encode('utf-8'))  # Encode the string to bytes
        print("Sent:", data.strip())
    except Exception as e:
        print("Error sending data:", e)

# Function to receive data
def receive_data():
    if uart1.any():  # Check if data is available
        return uart1.read()  # Read the data


while True:
    
    # Check for incoming data
    received = receive_data()
    if received:
        
        print("Raw Received Data:", received)  # Print raw bytes
        try:
            decoded_data = received.decode('utf-8')  # Decode bytes to string
            print("Received:", decoded_data.strip())  # Print the received data
        except Exception as e:
            print("Error decoding data:", e)
    else:
        print("No data received.")
    

    cmd = received

    if cmd == b'f':
        f1_pwm.duty_u16(int(65025*0.75))
        f2_pwm.duty_u16(int(65025*0.75))
        f3_pwm.duty_u16(int(65025*0.75))
        f4_pwm.duty_u16(int(65025*0.75))
        f5_pwm.duty_u16(int(65025*0.75))
        f6_pwm.duty_u16(int(65025*0.75))
        sleep(2)
       
    if cmd == b'w':
        led.toggle()
        (f1d,f2d,f3d,f4d,f5d,f6d) = (65025,65025,0,65025,65025,0)
    elif cmd == b's':
        (f1d,f2d,f3d,f4d,f5d,f6d) = (l,l,0,l,l,0)
    elif cmd == b'a':
        (f1d,f2d,f3d,f4d,f5d,f6d) = (l,65025,0,l,65025,0)
    elif cmd == b'd':
        (f1d,f2d,f3d,f4d,f5d,f6d) = (65025,l,0,65025,l,0)
    elif cmd == b'q':
        (f1d,f2d,f3d,f4d,f5d,f6d) = (0,0,65025,0,0,65025)
    elif cmd == b'e':
        (f1d,f2d,f3d,f4d,f5d,f6d) = (0,0,l,0,0,l)
    elif cmd == b'o':
        c1d += 1
        if c1d > 12:
            c1d = 0
        print(c1d)
    elif cmd == b'p':
        c1d -= 1
        if c1d < 0:
            c1d = 12
    elif cmd == b'x':
        c2d += 1
        if c1d > 30:
            c1d = 0
    elif cmd == b'c':
        c2d -= 1
        if c2d < 0:
            c2d = 30
    elif cmd == b'z':
        f1_pwm.deinit()
        f2_pwm.deinit()
        f3_pwm.deinit()
        f4_pwm.deinit()
        f5_pwm.deinit()
        f6_pwm.deinit()
        c1_pwm.deinit()
        
    
    c1_pwm.duty_u16(int((c1d/100)*65025))
    c2_pwm.duty_u16(int((c2d/1000)*65025))
    f1_pwm.duty_u16(f1d)
    f2_pwm.duty_u16(f2d)
    f3_pwm.duty_u16(f3d)
    f4_pwm.duty_u16(f4d)
    f5_pwm.duty_u16(f5d)
    f6_pwm.duty_u16(f6d)
    print(f1d,f2d,f3d,f4d,f5d,f6d)

