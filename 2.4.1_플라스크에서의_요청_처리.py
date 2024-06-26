from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested language: {language}"
