import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_add_integer(self):
        self.assertEqual(calculator.add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()