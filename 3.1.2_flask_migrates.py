from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_name'
db = SQLAlchemy(app)

# 여기서 모델 클래스를 정의헙니다.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
# Flask-Migrate 초기 설정
migrate = Migrate(app, db)

# 초기 설정
flask db init

# 마이그레이션 파일 생성 
flask db migrate -m "Initial migration."

# 마이그레이션 적용 
flask db upgrade

# 롤백 
flask db downgrade