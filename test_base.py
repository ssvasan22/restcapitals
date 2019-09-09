import argparse
import sys
import unittest

import base


class TestAPIResponse(unittest.TestCase):

    def test_city_name(self):
        city = "Berlin"
        result = base.get_capital_city_by_country("Germany")
        self.assertEqual(city, result)

    def test_city_name_another(self):
        city = "Ottawa"
        result = base.get_capital_city_by_country("India")
        self.assertNotEqual(city, result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("UT", help="input_value")
    parser.add_argument("unittest_args", nargs="*")
    args = parser.parse_args()
    sys.argv[1:] = args.unittest_args
    unittest.main()

