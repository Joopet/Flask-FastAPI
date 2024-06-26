from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fruits')
def show_fruits():
    # 여기에 테스트할 과일 목록을 넣습니다.
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    return render_template('fruits_list.html', fruits=fruits)