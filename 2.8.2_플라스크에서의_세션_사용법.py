from flask import Flask, session

app = Flask(__name__)

# 여기서 'your_secret_key'는 실제로는 안전하게 관리되어야 하는 민감한 정보입니다.
app.secret_key = 'your_secret_key'

# 세션 데이터 설정 라우트
@app.route('/set_session')
def set_session():
    session['username'] = 'SeungJoon'
    return '세션에 사용자 이름이 설정되었습니다!'

@app.route('/get_session')
def get_session():
    username = session.get('username')
    if username:
        return f'사용자 이름: {username}'
    else :
        return '사용자 이름이 세션에 설정되지 않았습니다.'
    
@app.route('/protected')
def protected():
    # 세션에 'username'이 설정되어 있지 않으면 403 Forbidden 에러를 반환합니다.
    if 'username' not in session:
        abort(403)
        return '이 페이지는 로그인한 사용자만 볼 수 있습니다!'
    else : 
        return '로그인된 페이지입니다!'