from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

@app.route('/')
def flask():
   GPIO.setmode(GPIO.BCM)        # setmode를 BCM으로 설정
   GPIO.setup(ledPin, GPIO.OUT)  # 21번핀을 설정
   GPIO.output(ledPin, 0)        # 처음에는 일단 꺼둔 상태
   return "Hello Flask"

@app.route('/led/on')
def ledOn():
   GPIO.output(ledPin, 1)        # LED 킴
   return "<h1> LED ON </h1> "

@app.route('/led/off')
def LedOff():
   GPIO.output(ledPin, 0)        # LED 끔
   return "<h1> LED OFF </h1>"

@app.route('/led/clean')
def clean():
   GPIO.cleanup()                 # 핀을 클린시키는 코드
   return "<h1> GPIO Clean </h1>"

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = "8080")