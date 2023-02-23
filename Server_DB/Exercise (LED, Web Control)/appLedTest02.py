from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def ledFlask():
   return "<h1> LED Control WepPage </h1>"

@app.route('/led/<state>')  # /이 매개변수로 와야함, 동적라우팅 함수 작성
def led(state):             # state를 매개변수로 받고 문자열에따른 조건문 작성
   if(state == 'on'):
      GPIO.output(ledPin, 1)  # LED 키고
   else:
      GPIO.output(ledPin, 0)  # LED 끄고
   return ("<h1> LED %s </h1>" %state)

@app.route('/led/clean')
def clean():
   GPIO.output(ledPin, GPIO.LOW)
   GPIO.cleanup()
   return "<h1> GPIO Clean!! </h1>"

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = "8080")