# import unittest
import sys
import os

sys.path.append(os.path.abspath('.'))

from app import template_hello


def test_hello_world():
    assert template_hello() == "<p>Hello, World!</p>"
    assert template_hello() != "<p>Hello, World</p>"


# class TestStringMethods(unittest.TestCase):

#     def test_hello(self):
#         self.assertEqual(template_hello(), "<p>Hello, World!</p>")
#         self.assertNotEqual(template_hello(), "<p>Hello, World</p>")

#     # def test_api_call(self):
#     #     url = "http://localhost:5000"
#     #     response = requests.get(url)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertNotEqual(response.status_code, 403)
#     #     self.assertEqual(response.text, "<p>Hello, World!</p>")

# if __name__ == '__main__':
#     pytest.main
