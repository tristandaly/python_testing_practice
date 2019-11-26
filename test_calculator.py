import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_add_integer(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_float(self):
        self.assertEqual(calculator.add(2.2, 44.4), 46.6)

    def test_subtract_integer(self):
        self.assertEqual(calculator.subtract(9, 5), 4)               

if __name__ == '__main__':
    unittest.main()