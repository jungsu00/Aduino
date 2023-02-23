# 파일이름 : flaskTest.py
from flask import Flask, render_template  
# from: Flask 폴더에서 flask모듈을 import(수입)하겠다는 뜻
# render_tempate 모듈을 import(수입)하겠다

app = Flask(__name__)       
# Flask라는 이름의 객체 생성


@app.route('/')             
# 클라이언트가 ui창에다가 /로 접속하면 hello함수 호출

def hello():                
   # /로 실행하면 호출되는 뷰함수
   # return "Hello World!"
   return render_template("index.html")     
   # 뷰함수는 반드시 retrun이 있어야한다.


if __name__ == "__main__":  
   # 직접 main을 실행시키기위한 조건

   app.run(host="0.0.0.0", port = "8080")