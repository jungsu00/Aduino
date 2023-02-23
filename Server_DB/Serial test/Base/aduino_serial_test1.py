import serial

ser = serial.Serial('/dev/ttyAMA0', 9600) # 시리얼 포트와 통신 속도 설정

while True:
    if ser.readable():
        data = ser.readline().decode() # 시리얼 포트로부터 데이터 받기
        print(data)