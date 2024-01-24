import unittest
import sys
import os
sys.path.append(os.path.abspath('.'))

from app import template_hello, divide



# =============== pytest ====================================
def test_hello_world():
    assert template_hello() != "<p>Hello, Worl</p>"
    assert template_hello() != "<p>Helo, World!</p>"


def test_divide(self):
    assert divide(10, 5) == 2
    assert divide(10, 1) == 10

    try:
        divide(10, 0)
        assert False
    except ZeroDivisionError:
            assert True


# =============== unittest ====================================
class TestFunc(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(template_hello(), "<p>Hello, World!</p>")
        self.assertNotEqual(template_hello(), "<p>Hello, Worl</p>")
        self.assertNotEqual(template_hello(), "<p>Helo, World!</p>")


    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(10, 1), 10)

        try:
            divide(10, 0)
            self.assertTrue(False)
        except ZeroDivisionError:
            self.assertTrue(True)