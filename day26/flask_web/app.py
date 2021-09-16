# 웹 서버(로컬) 가동

from flask import Flask

app = Flask(__name__)   # Flask 클래스에서 app 객체 생성

@app.route('/')   # 라우트(경로 설정)
def index():
    return "<h1>Hello Flask</h1>"   # 인덱스페이지에서 문자 출력

@app.route('/login')
def login():
    return "<h2>로그인 페이지 입니다.</h2>"

@app.route('/member')
def member():
    return "<h2>회원 가입 페이지 입니다.</h2>"

app.run()