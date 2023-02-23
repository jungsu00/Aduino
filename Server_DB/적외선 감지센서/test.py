import RPi.GPIO as GPIO

infrared = 20
ledPin = 21
                               
GPIO.setmode(GPIO.BCM)        # setmode를 BCM으로 설정
GPIO.setup(infrared, GPIO.IN) # 적외선 장애물 감지 센서 설정
GPIO.setup(ledPin, GPIO.OUT)  # LED 21번핀을 설정
GPIO.output(ledPin, 0)        # 처음에는 일단 꺼둔 상태

while 1:
    state = GPIO.input(infrared)

    if(state == False):
        GPIO.output(ledPin, 1)        # LED 킴

    else:
        GPIO.output(ledPin, 0)        # LED 끔