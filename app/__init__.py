# import requests
import json
from flask import Flask


app = Flask(__name__)



def template_hello():
    return "<p>Hello, World! ver2</p>"


@app.route("/")
def hello_world():
    return template_hello()


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2




# def hello_world():
#     response = requests.get(url, headers=header)
#     data = json.loads(response.text)
#     print(response.status_code)
#     return response.status_code



# if __name__ == '__main__':
#     hello_world()
