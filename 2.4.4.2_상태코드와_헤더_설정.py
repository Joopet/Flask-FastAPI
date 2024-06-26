from flask import Flask, make_response

app = Flask(__name__)

@app.route('/direct')
def direct_response():
    headers = {'X-Example': 'DirectHeader'}
    return make_response("Direct Response", 200, headers)
