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
        self.assertTrue('Array length is not sufficient to return two numbers' in str(context.exception))

    # Test when array contains string element
    def test_rearrange_digits_when_one_element_is_string(self):
        array = [4, 'a', 2, 5, 9, 8]
        with self.assertRaises(Exception) as context:
            ArrayDigits.rearrange_digits(array)
        self.assertTrue('Either the array contains non integer elements or integer is more than 9' in str(context.exception))

    # Test when array contains float
    def test_rearrange_digits_when_one_element_is_float(self):
        array = [4, 3.0, 2, 5, 9, 8]
        with self.assertRaises(Exception) as context:
            ArrayDigits.rearrange_digits(array)
        self.assertTrue('Either the array contains non integer elements or integer is more than 9' in str(context.exception))

    # Test when array is empty
    def test_rearrange_digits_when_array_is_empty(self):
        array = []
        with self.assertRaises(Exception) as context:
            ArrayDigits.rearrange_digits(array)
        self.assertTrue('Array length is not sufficient to return two numbers' in str(context.exception))

    # Test when array contains two digited element as integer
    def test_rearrange_digits_when_one_element_is_two_digited(self):
        array = [4, 30, 2, 5, 9, 8]
        with self.assertRaises(Exception) as context:
            ArrayDigits.rearrange_digits(array)
        self.assertTrue('Either the array contains non integer elements or integer is more than 9' in str(context.exception))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArrayDigits)
    unittest.TextTestRunner(verbosity=2).run(suite)