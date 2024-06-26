from flask import Flask, make_response

app = Flask(__name__)

@app.route('/custom')
def custom_response():
    response = make_response("Custom Response", 202)
    response.headers['X-Example'] = 'CustomHeader'
    return response