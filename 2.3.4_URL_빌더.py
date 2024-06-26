from flask import Flask, url_for

app = Flask(__name__)

# 뷰 함수: 사용자 프로필을 보여줍니다.
@app.route('/user/<username>')
def show_user_profile(username):
    # 실제로는 사용자 프로필 정보를 보여주는 로직이 위치할 것이다.
    return f'User {username}'

# 뷰 함수: 게시물을 보여줍니다.
@app.route('/post/<year>/<month>/<day>')
def show_post(year, month, day):
    # 실제로는 해당 날짜에 해당하는 게시물을 보여주는 로직이 위치할 것입니다.
    return f'Post for {year}/{month}/{day}'

# 홈페이지에서 url_for를 이용하여 위의 뷰 함수들로 이동하는 링크를 생성합니다. 
@app.route('/')
def index():
    # 'show_user_profile' 뷰로 이동하는 URL을 생성합니다.
    user_url = url_for('show_user_profile', username='seungjoon')
    # 'show_post' 뷰로 이동하는 URL을 생성합니다.
    post_url = url_for('show_post', year='2023', month='04', day='01')
    # 생성된 URL을 반환합니다.
    return f'User URL: {user_url}<br>Post URL: {post_url}'