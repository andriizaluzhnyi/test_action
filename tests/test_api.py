# import unittest
import sys
import os
sys.path.append(os.path.abspath('.'))

from app import template_hello, divide


def test_hello_world():
    assert template_hello() == "<p>Hello, World!</p>"
    assert template_hello() != "<p>Hello, World</p>"
    assert template_hello() != "<p>Helo, World!</p>"


def test_divide():
    assert divide(10, 5) == 2
    assert divide(10, 1) == 10

    try:
        divide(10, 0)
        assert False
    except ZeroDivisionError:
        assert True
