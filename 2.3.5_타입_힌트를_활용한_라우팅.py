# 타입 힌트를 이용한 라우팅 

@app.route('/int/<int:var>')
def int_type(var:int):
    return f'Integer: {var}'

@app.route('/float/<float:var>')
def float_type(var:float):
    return f'Float: {var}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

@app.route('/uuid/<uuid:some_id>')
def show_uuid(some_id):
    return f'UUID: {some_id}'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return 'test'


