from flask import Flask, request

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_user():
    if request.method == 'GET':
        # GET 요청 처리 로직
        return "USER data"
    elif request.method == 'POST':
        # POST 요청 처리 로직
        return "Create user"
    elif request.method == 'PUT':
        # PUT 요청 처리 로직
        return "Update user"
    elif request.method == 'DELETE':
        # DELETE 요청 처리 로직
        return "Delete user"