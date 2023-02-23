# 라즈베리파이에서 적외선 센서를 인식하여 
# Atmega328p로 servo_motor 작동

import RPi.GPIO as GPIO          # Raspi GPIO선 사용 코드

infrared = 20                    # 적외선 out선을 GPIO 20번에 연결
                               
GPIO.setmode(GPIO.BCM)           # setmode를 BCM으로 설정
GPIO.setup(infrared, GPIO.IN)    # 적외선 장애물 감지 센서 설정

while 1:
    state = GPIO.input(infrared) # 적외선 센서값을 state로 설정

    if(state == False):          # state값 0일 때(0 == 물체 감지)
        print(state)             # state값 출력

    else:                        # state값 0이 아닐 때(0 /= 물체 미감지)
        print(state)