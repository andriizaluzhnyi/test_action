# import unittest
import sys
import os

sys.path.append(os.path.abspath('.'))

from app import template_hello


def test_hello_world():
    assert template_hello() == "<p>Hello, World!</p>"
    assert template_hello() != "<p>Hello, World</p>"
    assert template_hello() != "<p>Helo, World!</p>"
