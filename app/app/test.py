""" Sample Tests """

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ Calc Tests """

    def test_add_numbers(self):
        """ Test adding numbers together """

        result = calc.add(1, 2)

        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """ Test subtracting numbers together """

        result = calc.subtract(10, 15)

        self.assertEqual(result, -5)
