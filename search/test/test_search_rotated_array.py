import unittest
from search_rotated_array import SearchRotatedArray

class TestSearchRotatedArray(unittest.TestCase):
    def test_search_rotated_array_when_search_element_is_in_first_position(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6),
            SearchRotatedArray.linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)
        )
    def test_search_rotated_array_when_min_element_is_near_middle(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1),
            SearchRotatedArray.linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
        )
    def test_search_rotated_array_for_max_element_when_list_has_non_contiguous_numbers(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8),
            SearchRotatedArray.linear_search([6, 7, 8, 1, 2, 3, 4], 8)
        )
    def test_search_rotated_array_for_min_element_when_list_has_non_contiguous_numbers(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1),
            SearchRotatedArray.linear_search([6, 7, 8, 1, 2, 3, 4], 1)
        )

    def test_search_rotated_array_for_number_not_present(self):
        self.assertEqual(
            SearchRotatedArray.rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10),
            SearchRotatedArray.linear_search([6, 7, 8, 1, 2, 3, 4], 10)
        )

if __name__ == '__main__':
    unittest.main()
