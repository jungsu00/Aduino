import RPi.GPIO as GPIO
import serial
import time

py_serial = serial.Serial(
    port='/dev/ttyAMA0', # Raspqi port
    baudrate=9600,  # 보드 레이트 (통신 속도)
)

while True:
    time.sleep(0.1)

    commend = input('아두이노에게 내릴 명령:')
    py_serial.write(commend.encode())
    value = py_serial.write(commend.encode())