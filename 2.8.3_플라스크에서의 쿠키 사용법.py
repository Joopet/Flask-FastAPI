from flask import Flask, make_response, request, abort

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('쿠키를 설정합니다.')
    resp.set_cookie('username', 'SeungJoon')
    return resp

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', '게스트')
    return f'쿠키로부터 얻은 사용자 이름: {username}'

# 쿠기가 설정된 사용자만 접근 가능한 라우트
@app.route('/secret')
def secret():
    username = request.cookies.get('username')
    if not username:
        # 쿠키가 없다면 접근 금지 메시지 반환
        abort(403, description="접근 권한이 없습니다. 먼저 쿠키를 설정해주세요.")
    return f'환영합니다, {username}님! 비밀 페이지에 접속하셨습니다.'

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('쿠키를 삭제합니다.')
    resp.delete_cookie('username')
    return resp

# max_age 옵션 : 쿠키가 유지될 시간을 초 단위로 설정
# resp.set_cookie('username', 'SeungJoon', max_age=60*60*24*7)

# expires 옵션 : 쿠키가 만료되는 정확한 날짜와 시간을 설정할 수 있다. 
# resp.set_cookie('username', 'SeungJoon', expires=datetime.datetime(2027, 11, 7))

# path 옵션 : 쿠키의 유효 경로를 제한할 . 수있다. 위 코드는 '/app' 경로와 이 경로의 하위 경로에서만 쿠키가 유효하게 됩니다. 
# resp.set_cookie('username', 'SeungJoon', path='/app')

# domain 옵션 : 쿠키가 특정 도메인에서 유효하게 됩니다. 위 코드는 '.example.com' 도메인과 그 하위 도메인에서 쿠키를 사용할 수 있게 합니다. 
# resp.set_cookie('username', 'SeungJoon', domain='.example.com')

# secure 옵션 : secure 옵션이 True로 설정되면, 쿠키는 HTTPS 연결을 통해서만 전송됩니다. 이는 쿠키가 암호화되어 안전하게 전송되도록 보장
# resp.set_cookie('username', 'SeungJoon', secure=True)

# httponly 옵션 : 쿠키는 웹서버를 통해서만 접근할 수 있습니다. 클라인언트 사이트 스크립트, 예를 들어 자바스크립트는 쿠키에 접근할 수 없게 되어 보안을 강화 합니다. 
# resp.set_cookie('username', 'SeungJoon', httponly=True)


