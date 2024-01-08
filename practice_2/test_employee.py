import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.labor = Employee('David', 'wang', 30000)

    def test_give_default_raise(self):
        self.salary = self.labor.give_raise()
        self.assertEqual(self.salary, 35000)

    def test_give_custom_raise(self):
        self.salary = self.labor.give_raise(10000)
        self.assertEqual(self.salary, 40000)
