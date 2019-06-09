import unittest
"""
Implements searching in a rotated array
"""
class SearchRotatedArray:
    """
    Parameters:
        input_list: List of integers to be searched
        number: Integer number to be searched in the input list
    Returns:
        -1 if the number is not found in the list
        index position of the number in the list
    """
    @staticmethod
    def rotated_array_search(input_list, number):
        # validate input parameters
        if not (isinstance(input_list, list) and all(isinstance(x, int) for x in input_list)):
            raise Exception('The first parameter needs to be a list of integer')
        if not isinstance(number, int):
            raise Exception('Second parameter needs to an integer')
        # If input_list is empty, then return
        if len(input_list) == 0:
            return -1
        # Find the position of the max value in the list
        max_index = SearchRotatedArray.find_max_index(input_list, 0, len(input_list) - 1)
        # Implement binary search
        if input_list[max_index] == number:
            return max_index
        elif input_list[max_index] < number:
            return -1
        else:
            # Invoke binart search of an ascendingly ordered array for the elements in the index positions [0..max_index - 1]
            if number < input_list[max_index - 1] and input_list[0] <= number:
                return SearchRotatedArray.ascending_binary_search(input_list, 0, max_index - 1, number)
            else:
                # Invoke binart search of an ascendingly ordered array for the elements in the index positions [max_index + 1:]
                return SearchRotatedArray.ascending_binary_search(input_list, max_index + 1, len(input_list) - 1, number)

    # Binary search an array when the elements are in ascending order
    @staticmethod
    def ascending_binary_search(input_list, left, right, number):
        if left > right:
            return -1
        else:
            mid = int((left + right) / 2)
            if input_list[mid] == number:
                return mid
            elif input_list[mid] >= number:
                return SearchRotatedArray.ascending_binary_search(input_list, left, mid, number)
            else:
                return SearchRotatedArray.ascending_binary_search(input_list, mid + 1, right, number)

    # Finds the index position of maximum value in the list
    @staticmethod
    def find_max_index(input_list, left, right):
        if left > right: \
                return -1
        else:
            if left == right:
                return left
            elif left + 1 == right:
                return left if input_list[left] >= input_list[left + 1] else left + 1
            else:
                mid = int((left + right) / 2)
                # Element at index = mid is greater than element to its left & right
                if input_list[mid] > input_list[mid - 1] and input_list[mid] > input_list[mid + 1]:
                    return mid
                # Element as index = mid is less than element to its left and its right
                # Then max element is at position (mid - 1)
                elif input_list[mid - 1] > input_list[mid] and input_list[mid] < input_list[mid + 1]:
                    return mid - 1
                # Pivot point appears on the left
                elif input_list[0] > input_list[mid + 1]:
                    return SearchRotatedArray.find_max_index(input_list, left, mid - 1)
                # Ascending section of the array
                else:
                    return SearchRotatedArray.find_max_index(input_list, mid + 1, right)

    # Implements linear search. Used for running the unit tests
    @staticmethod
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

# Unit test
class TestSearchRotatedArray(unittest.TestCase):

    # First parameter is not a list
    def test_search_rotated_array_when_first_parameter_is_not_list(self):
        with self.assertRaises(Exception) as context:
            SearchRotatedArray.rotated_array_search(6, 4)
        self.assertTrue('The first parameter needs to be a list of integer' in str(context.exception))

    # Element to be searched is not an integer
    def test_search_rotated_array_when_second_parameter_is_not_int(self):
        with self.assertRaises(Exception) as context:
            SearchRotatedArray.rotated_array_search([6, 2], 'a')
        self.assertTrue('Second parameter needs to an integer' in str(context.exception))

    # Element to be searched is in the first position
    def test_search_rotated_array_when_search_element_is_in_first_position(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6),
            SearchRotatedArray.linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)
        )

    # Pivot point is near the middle of the list
    def test_search_rotated_array_when_min_element_is_near_middle(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1),
            SearchRotatedArray.linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
        )

    # Elements in the list are non contiguous and the element to be searched is the maximum element in the list
    def test_search_rotated_array_for_max_element_when_list_has_non_contiguous_numbers(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8),
            SearchRotatedArray.linear_search([6, 7, 8, 1, 2, 3, 4], 8)
        )

    # Elements in the list are non contiguous and the element to be searched is the minimum element in the list
    def test_search_rotated_array_for_min_element_when_list_has_non_contiguous_numbers(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1),
            SearchRotatedArray.linear_search([6, 7, 8, 1, 2, 3, 4], 1)
        )

    # Test searching for an element when in the element is not present in the list
    def test_search_rotated_array_for_number_not_present(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10),
            SearchRotatedArray.linear_search([6, 7, 8, 1, 2, 3, 4], 10)
        )

    # Test searching for the element when the element is at the first position of rotated array
    def test_search_rotated_array_pivot_point_is_at_the_start(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
            SearchRotatedArray.linear_search([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        )

    # Test when there are two elements in the list
    def test_search_rotated_array_with_two_element(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([10, 1], 10),
            SearchRotatedArray.linear_search([10, 1], 10)
        )

    # Test when there is only one element in the list
    def test_search_rotated_array_with_one_element(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([11], 11),
            SearchRotatedArray.linear_search([11], 11)
        )

    # Test when there is no element in the list
    def test_search_rotated_array_zero_element(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([], 11),
            SearchRotatedArray.linear_search([], 11)
        )

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchRotatedArray)
    unittest.TextTestRunner(verbosity=2).run(suite)

