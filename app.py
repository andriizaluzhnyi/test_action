from flask import Flask

from app import template_hello

app = Flask(__name__)


@app.route("/")
def hello_world():
    return template_hello
