from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.methods == "POST":
        return "Logging in..."
    else :
        return "Login Form"