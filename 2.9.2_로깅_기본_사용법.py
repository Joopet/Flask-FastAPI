from flask import Flask

app = Flask(__name__)

# 로그 레벨 설정
# DEBUG : 가장 낮은 레벨로, 상세한 정보를 기록할 때 사용. 개발 중에 문제를 진달할 때 유용합니다.
# INFO : 일반적인 정보를 기록하는데 사용합니다.
# WARNING : 예상치 못한 일이 발생했거나 문제가 발생할 가능성이 있는 경우에 사용됩니다. 
# ERROR : 심각한 문제로, 프로그램의 일부 기능이 제대로 작동하지 않을 때 사용됩니다.
# CRITICAL : 매우 심각한 문제로, 애플리케이션이 계속 실행될 수 없을 때 사용됩니다. 

import logging
app.logger.setLevel(logging.DEBUG) # DEBUG 레벨 로깅 활성화 

logging.basicConfig(filename='application.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.route('/')
def home():
    # 여기서 각기 다른 로그 레벨의 로그를 생성합니다.
    app.logger.debug('Debug level log')     # 디버그 메시지
    app.logger.info('Info level log')       # 정보 메시지
    app.logger.warning('Warning level log') # 경고 메시지
    app.logger.error('Error level log')     # 에러 메시지
    app.logger.critical('Critical level log')   # 크리티컬 메시지
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)