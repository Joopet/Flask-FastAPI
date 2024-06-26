from flask import Flask, render_template

app = Flask(__name__, static_url_path='/img', static_folder='static/img')

@app.route('/')
def home():
    return render_template('index.html')
