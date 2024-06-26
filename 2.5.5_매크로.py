from flask import Flask, render_template

app = Flask(__name__)

@app.route('/messages')
def show_messages():
    # 여기에 테스트할 과일 목록을 넣습니다.
    return render_template('messages.html')