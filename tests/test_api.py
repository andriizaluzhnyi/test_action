import unittest
import requests



class TestStringMethods(unittest.TestCase):

    def test_api_call(self):
        url = "http://localhost:5000"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 403)
        self.assertEqual(response.text, "<p>Hello, World!</p>")

if __name__ == '__main__':
    unittest.main
