from flask import Flask

def template_hello():
    return "<p>Hello, World!</p>"

app = Flask(__name__)


@app.route("/")
def hello_world():
    return template_hello
