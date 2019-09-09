import sys
import unittest
from sys import argv

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
    unittest.main(sys.argv[1])

