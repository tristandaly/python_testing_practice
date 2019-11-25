import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_add_integer(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_float(self):
        self.assertEqual(calculator.add(2.2, 44.4), 46.6)

class ExpectedFailureTestCalculator(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail_add_string(self):
        self.assertEqual(calculator.add("Butt ", "Head"), "Butt Head")             

if __name__ == '__main__':
    unittest.main()