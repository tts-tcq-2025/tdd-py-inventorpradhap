import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(StringCalculator().add(""), 0)

    def test_single_number_returns_itself(self):
        self.assertEqual(StringCalculator().add("1"), 1)

    def test_two_numbers_comma_separated_returns_sum(self):
        self.assertEqual(StringCalculator().add("1,2"), 3)

    def test_multiple_numbers_comma_separated_returns_sum(self):
        self.assertEqual(StringCalculator().add("1,2,3,4"), 10)

    def test_new_lines_between_numbers_returns_sum(self):
        self.assertEqual(StringCalculator().add("1\n2,3"), 6)

    def test_different_delimiter_returns_sum(self):
        self.assertEqual(StringCalculator().add("//;\n1;2"), 3)

    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError):
            StringCalculator().add("1,-2")

    def test_numbers_bigger_than_1000_ignored(self):
        self.assertEqual(StringCalculator().add("2,1001"), 2)

    def test_delimiters_of_any_length(self):
        self.assertEqual(StringCalculator().add("//[***]\n1***2***3"), 6)

if __name__ == '__main__':
    unittest.main()
