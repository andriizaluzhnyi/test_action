
def template_hello():
    return "<p>Hello, World!</p>"


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2
