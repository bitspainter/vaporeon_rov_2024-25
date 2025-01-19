import sys
from time import sleep
from machine import UART

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
    msg = input()
    send_data(msg)
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

