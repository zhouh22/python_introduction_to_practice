import city_functions as cif
import unittest


class TestCases(unittest.TestCase):

    def test_city_country(self):
        result = cif.city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago,Chile")

    def test_city_country_population(self):
        result = cif.city_country("Santiago", "Chile", 5000000)
        self.assertEqual(result, "Santiago,Chile - population 5000000")


if __name__ == '__main__':
    unittest.main()
