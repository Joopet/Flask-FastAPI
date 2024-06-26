from flask import Flask, render_template

app = Flask(__name__)

# 메일 페이지 라우트
@app.route('/img/<path:filename>')
def custom_static(filename):
    return render_template('static/img', filename)

@app.route('/')
def home():
    return render_template('index2.html')