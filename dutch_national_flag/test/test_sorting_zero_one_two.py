import unittest
from sorting_zero_one_two import ZeroOneTwoSorter

class TestZeroOneTwoSorter(unittest.TestCase):
    def test_sort_with_array_starting_with_zero_ending_with_two(self):
        self.assertEqual(ZeroOneTwoSorter.sort([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]), [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2])

    def test_sort_with_array_starting_with_two_ending_with_one(self):
        self.assertEqual(
            ZeroOneTwoSorter.sort(
                [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
            ),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        )


    def test_sort_already_sorted_array(self):
        self.assertEqual(
            ZeroOneTwoSorter.sort(
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
            ),
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        )

if __name__ == '__main__':
    unittest.main()