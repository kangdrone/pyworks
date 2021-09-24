from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>안녕하세요~ index 화면입니다.</h1>"
    return render_template('index.html')

@app.route('/input', methods=["GET"])   # get 방식
def input():
    return render_template('input.html')

@app.route('/output', methods=['POST'])   # post 방식
def output():
    uid = request.form['uid']   # name 값을 가져옴
    pwd = request.form['passwd']
    return render_template('output.html', uid = uid, pwd = pwd)

@app.route('/input_num', methods=['GET'])
def input_num():
    return render_template('input_num.html')

# 짝수/홀수 판정 프로그램
@app.route('/even_odd', methods=['POST'])
def even_odd():
    num = int(request.form['num'])   # 입력된 숫자를 받아옴
    if num % 2 == 0:
        result = "짝수입니다."
    else:
        result = "홀수입니다."
    return render_template('even_odd.html', num = num, result = result)


    # 딕셔너리의 key=value 구조임
app.run()