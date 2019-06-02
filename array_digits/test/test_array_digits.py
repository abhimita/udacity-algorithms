import unittest
from array_digits import ArrayDigits

class TestArrayDigits(unittest.TestCase):
    def test_rearrange_digits_when_odd_number_of_elements(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayDigits.rearrange_digits(array), [542, 31])

    def test_rearrange_digits_when_even_number_of_elements(self):
        array = [4, 6, 2, 5, 9, 8]
        self.assertEqual(ArrayDigits.rearrange_digits(array), [964, 852])

    def test_rearrange_digits_when_two_elements(self):
        array = [4, 6]
        self.assertEqual(ArrayDigits.rearrange_digits(array), [6, 4])

if __name__ == '__main__':
    unittest.main()