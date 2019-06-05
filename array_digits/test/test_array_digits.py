import unittest
from array_digits import ArrayDigits

class TestArrayDigits(unittest.TestCase):
    # Test when there are odd number of digits in the given array
    def test_rearrange_digits_when_odd_number_of_elements(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayDigits.rearrange_digits(array), [542, 31])

    # Test when there are even number of digits in the given array
    def test_rearrange_digits_when_even_number_of_elements(self):
        array = [4, 6, 2, 5, 9, 8]
        self.assertEqual(ArrayDigits.rearrange_digits(array), [964, 852])

    # Test when there are only two elements in the array
    def test_rearrange_digits_with_two_elements(self):
        array = [4, 6]
        self.assertEqual(ArrayDigits.rearrange_digits(array), [6, 4])

    # Test when there is only one element. This will throw an exception.
    def test_rearrange_digits_with_one_element(self):
        array = [4]
        with self.assertRaises(Exception) as context:
            ArrayDigits.rearrange_digits(array)
            self.assertTrue('Array length is no sufficient to return two numbers' in context.exception)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArrayDigits)
    unittest.TextTestRunner(verbosity=2).run(suite)