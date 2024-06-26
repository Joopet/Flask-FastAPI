from flask_login import LoginManager

# LoginManager 인스턴스 생성 
login_manager = LoginManager()
# Flask 애플리케이션과 LoginManager 인스턴스 연결
login_manager.init_app(app)