import unittest


"""
Class that solves the problem of generating two numbers from integers in the array
so that the sum of the two number is maximum obeying the constraints listed in the problem
"""
class ArrayDigits:
    """
    Parameters:
        array: Array containing the digits from which two numbers need to be formed
    Returns:
        two integers whose sum is maximum
    """
    @staticmethod
    def rearrange_digits(array):
        # Array should contain list of single digit integers
        if not all(isinstance(x, int) and x in range(0, 10) for x in array):
            raise Exception("Either the array contains non integer elements or integer is more than 9")
        sz = len(array)
        # Array should be at least of length = 2
        if sz <= 1:
            raise Exception("Array length is not sufficient to return two numbers")
        # Sort the array in descending order
        MergeSort.sort(array)
        first = ''
        second = ''
        # If the array contains odd number of integers then one of the two numbers
        # will have one extra digit position compared to the other one
        if sz % 2 != 0:
            # Pick up the largest integer for the leading digit of the first number
            first = str(array[0])
            start_index = 1
        else:
            start_index = 0
        # Highest values pulled out from descending sorted array
        # Alternate these integers to be used in consecutive leading place
        # values for first and second numbers with place values being filled
        # from left to right
        for index, element in enumerate(array[start_index:]):
            if index % 2 == 0:
                first += str(element)
            else:
                second += str(element)
        return [int(first), int(second)]

"""
Implements Merge sort. Sorting is done in-place.
"""
class MergeSort:
    """
    Parameters:
        array: Array to be sort
    """
    @staticmethod
    # Recursive method for merge sort
    def sort(array):
        # Sorting is needed only when array contains more than one element
        if len(array) > 1:
            # Determine mid of the array
            mid = len(array) // 2
            first = array[:mid]
            second = array[mid:]
            # Recursively call merge sort for the first half of the array
            MergeSort.sort(first)
            # Recursively call merge sort for second half of the array
            MergeSort.sort(second)
            # Merge two sorted arrays
            MergeSort.merge(first, second, array)

    """
    Merges two sorted arrays. Final array is sorted in descending order
    Parameters:
        first: First array
        second: Second array
        array: Array containing descending sorted numbers   
    """
    @staticmethod
    def merge(first, second, array):
        len_first = len(first)
        len_second = len(second)
        i = j = k = 0
        while i < len_first and j < len_second:
            # Descending sort
            # Pick up elements from first array when the element is greater
            # than the current element in second array
            if first[i] >= second[j]:
                array[k] = first[i]
                i += 1
            else:
                # Pick up element from second array
                array[k] = second[j]
                j += 1
            k += 1
        # Pick up any residual elements form first array which didn't make it to final array
        while i < len_first:
            array[k] = first[i]
            i += 1
            k += 1
        # Pick up any residual elements form second array which didn't make it to final array
        while j < len_second:
            array[k] = second[j]
            k += 1
            j += 1

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