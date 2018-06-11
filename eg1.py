from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/tiide")
def tiide():
    return "welcome to tiide world"
