import unittest
from sorting_zero_one_two import ZeroOneTwoSorter

class TestZeroOneTwoSorter(unittest.TestCase):
    # Array to be sorted as few zeros at the beginning and 2 at the end
    def test_sort_with_array_starting_with_zero_ending_with_two(self):
        self.assertEqual(ZeroOneTwoSorter.sort([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]), [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2])

    # Array to be sorted starts with 2 and ends with 1
    def test_sort_with_array_starting_with_two_ending_with_one(self):
        self.assertEqual(
            ZeroOneTwoSorter.sort(
                [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
            ),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        )

    # Array is already sorted
    def test_sort_already_sorted_array(self):
        self.assertEqual(
            ZeroOneTwoSorter.sort(
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
            ),
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        )

    # Array is to be sorted is empty (no elements)
    def test_sort_with_empty_array(self):
        self.assertEqual(ZeroOneTwoSorter.sort([]), [])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestZeroOneTwoSorter)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()