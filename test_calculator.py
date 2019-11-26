import calculator
import unittest

class TestCalculator(unittest.TestCase):
    # Addition
    def test_add_integer(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_float(self):
        self.assertEqual(calculator.add(2.2, 44.4), 46.6)
    # Subtraction
    def test_subtract_integer(self):
        self.assertEqual(calculator.subtract(9, 5), 4)

    def test_subtract_float(self):
        self.assertAlmostEqual(calculator.subtract(99.9, 88.8), 11.1)
    # Multiplication
    def test_multiply_integer(self):
        self.assertEqual(calculator.multiply(5, 5), 25)

    def test_multiply_float(self):
        self.assertEqual(calculator.multiply(30.9, 77.5), 2394.75)
    # Division
    def test_divide_integer(self):
        self.assertEqual(calculator.divide(10, 5), 2)

    def test_divide_integer_with_remainder(self):
        self.assertEqual(calculator.divide(10, 6), str(1.4))

if __name__ == '__main__':
    unittest.main()