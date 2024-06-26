from flask import Flask, request, url_for, session # 웹 애플리케이션과 세션 관리 
from flask_sqlalchemy import SQLAlchemy # ORM을 위한 플라스크 확장 
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user  # 사용자 인증 관리

# 플라스크 애플리케이션 인스턴스를 생성합니다. 
app = Flask(__name__)

# 데이터베이스 설정을 애플리케이션 설정에 추가합니다. 여기서는 MYSQL을 사용하고 있습니다. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

# SQLALchemy 인스턴스를 생성하고 애플리케이션을 바인딩합니다. 
db = SQLAlchemy(app)

# 로그인 관리자 인스턴스를 생성합니다. 
login_manager = LoginManager()
login_manager.init_app(app)     # 애플리케이션에 로그인 관리자를 적용합니다.
login_manager.login_view = 'login'  # 사용자가 로그인해야 하는 뷰를 설정합니다. 

# 데이터베이스 모델을 정의합니다. UserMixin은 Flask-Login에서 제공하는 기본 사용자 모델이다. 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)    # 사용자 ID
    username = db.Column(db.String(80), unique=True, nullable=False)    # 사용자 이름
    email = db.Column(db.String(120), unique=True, nullable=False)  # 이메일
    password = db.Column(db.String(128))    # 비밀번호

    # 객체의 문자열 표현을 정의합니다.
    def __repr__(self):
        return f'<User {self.username}>'

# 사용자 ID로 사용자를 로드하는 콜백 함수를 정의합니다.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 데이터베이스 테이블을 생성합니다.
with app.app_context():
    db.create_all()

# 인덱스 뷰를 정의합니다. '/' 경로로 접근할 경우 실행됩니다. 
@app.route('/')
def index():
    user_id = session.get('user_id')    # 세션에서 user_id를 가져옵니다. 
    if user_id:
        user = User.query.get(user_id)
        return f'Logged in as {user.username}'  # 로그인된 상태를 표시합니다. 
    return 'You are not logged in'  # 로그인되지 않은 상태를 표시합니다.


# 보호된 페이지를 위한 뷰를 정의합니다. 이 페이지는 로그인이 필요합니다.
@app.route('/protected')
@login_required # 로그인이 필요하다는 데코레이터입니다. 
def protected():
    # 현재 로그인한 사용자의 이름을 표시합니다.
    return f'Logged in as {current_user.username}'

# 로그인 뷰를 정의합니다. GET과 POST 메서드를 모두 처리합니다.
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # 폼데이터로부터 사용자 이름과 비밀번호를 가져옵니다.
        username = request.form['username']
        password = request.form['password']
        # 데이터베이스에서 사용자를 조회합니다. 
        user = User.query.filter_by(username=username).first()
        # 사용자가 존재하고 비밀번호가 맞다면
        if user and user.password == password:
            login_user(user)    # 사용자를 로그인시킵니다.
            session['user_id'] = user.id    # 세션에 user_id를 저장합니다. 
            return redirect(url_for('protected'))   # 보호된 페이지로 리다이렉트합니다.
        # 로그인 폼을 렌더링합니다.
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# 로그아웃 뷰를 정의합니다.
@app.route('/logout')
@login_required # 로그인이 필요하다는 데코레이터입니다. 
def logout():
    logout_user()   # 사용자를 로그아웃시킵니다.
    session.pop('user_id', None)    # 세션에서 user_id를 제거합니다.
    return redirect(url_for('index'))   # 인덱스 페이지로 리다이렉트합니다. 

# 테스트 사용자를 생성하는 뷰를 정의합니다. 
@app.route('/create_test_user')
def create_test_user():
    test_user = User(username='testuser', email='test@example.com', password='testpassword')
    db.session.add(test_user)   # 세션에 추가합니다. 
    db.session.commit()         # 변경 사항을 커밋합니다.
    return 'Test user created'  # 테스트 사용자가 생성되었다는 메시지를 출력합니다. 



