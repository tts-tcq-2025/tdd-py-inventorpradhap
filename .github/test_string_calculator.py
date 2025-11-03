import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_itself(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers_comma_separated(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)

    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")

    def test_multiple_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2, -3")

    def test_numbers_bigger_than_1000_ignored(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)

    def test_custom_delimiter_any_length(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

if __name__ == '__main__':
    unittest.main()