import unittest
from my_app import app  # my_app 모듈에서 플라스크 애플리케이션을 가져옵니다. 

# Basic TestCase 클래스는 unittest.TestCase를 상속받습니다. 
class BasicTestCase(unittest.TestCase):

    # index 리우트를 테스트하는 메서드입니다. 
    def test_index(self):
        # 플라스크 애플리케이션을 위한 테스트 클라이언트 인스턴스를 생성합니다. 
        tester = app.test_client(self)
        # 테스트 클라이언트를 사용하여 루트 URL로 GET 요청을 보냅니다.
        response = tester.get('/', content_type='html/text')
        # 응답받은 상태 코드가 200인지 확인합니다.
        self.assertEqual(response.status_code, 200)

class AdvancedTestCase(unittest.TestCase):

    def setUp(self):
        # 플라스크 애플리케이션의 테스트 클라이언트를 생성합니다.
        # self.tester는 테스트 동안 사용할 가상의 클라이언트 객체입니다. 
        self.tester = app.test_client(self)

    def tearDown(self):
        # 테스트가 끝난 후 정리 작업을 수행합니다. 현재는 비어 있는 상태입니다.
        pass

    def test_index(self):
        # self.tester 객체를 사용하여 루트 URL('/')로 HTTP GET 요청을 보냅니다. 
        response = self.tester.get('/', content_type='html/text')
        # 응답의 상태 코드가 200인지 확인합니다.
        self.assertEqual(response.status_code, 200)
    # test_index_text 메서드는 루트 경로의 응답 텍스트를 테스트합니다.
    def test_index_text(self):
        # 루트 경로에 GET 요청을 보내고 응답 데이터를 검증합니다.
        response = self.tester.get('/', content_type='html/text')
        #응답 데이터가 'Hello, World!'와 일치하는지 바이트 문자열로 확인합니다.
        self.assertEqual(response.data, b'Hello, World!')
    
    # test_another_route 메서드는 다른 경로('/another')에 대한 테스트를 정의합니다.
    def test_another_route(self):
        # '/another' 경로에 GET 요청을 보내고 상태 코드를 검증합니다.
        response = self.tester.get('/another', content_type='html/text')
        # 해당 경로가 존재하지 않으므로 상태 코드가 404(찾을 수 없음)인지 확인합니다.
        self.assertEqual(response.status_code, 404)


