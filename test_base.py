import argparse
import sys
import unittest

import base


class TestAPIResponse(unittest.TestCase):

    def test_valid_city_name(self):
        self.assertEqual(base.get_capital_city_by_country("germany"), "Berlin")

    def test_invalid_city_name(self):
        self.assertNotEqual(base.get_capital_city_by_country("australia"), "Bogota")

    def test_invalid_city_string(self):
        self.assertNotEqual(base.get_capital_city_by_country("234"), "Invalid URL. Server returned 404")

    def test_valid_code_city_name(self):
        self.assertEqual(base.get_capital_city_by_code("au"), "Canberra")

    def test_invalid_code_city_name(self):
        self.assertNotEqual(base.get_capital_city_by_code("au"), "Berlin")

    def test_code_validation(self):
        exception_message = "Bad Request"
        error_message = base.get_capital_city_by_code("romania")
        self.assertEqual(error_message, exception_message)

    def test_code_number(self):
        self.assertNotEqual(base.get_capital_city_by_code("123"), "Bad Request Exception")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("UT", help="input_value")
    parser.add_argument("unittest_args", nargs="*")
    args = parser.parse_args()
    sys.argv[1:] = args.unittest_args
    unittest.main()
