import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_add_integer(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_float(self):
        self.assertEqual(calculator.add(2.2, 44.4), 46.6)    

if __name__ == '__main__':
    unittest.main()