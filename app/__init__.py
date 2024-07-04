# import requests
import json
from flask import Flask


app = Flask(__name__)



def template_hello():
    return "<p>Hello, World!</p>"


@app.route("/")
def hello_world():
    return template_hello()


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

