import unittest
from search_rotated_array import SearchRotatedArray

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
