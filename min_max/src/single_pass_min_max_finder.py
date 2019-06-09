import unittest
import random

"""
Class that find min and max in an integer array in a single pass
"""
class SinglePassMinMaxFinder:
    """
    Parameters:
        ints: List of integers which is used to min & max in a single pass
    Returns:
        two integers: min value & max value
    """
    @staticmethod
    def get_min_max(ints):
        if len(ints) == 0:
            raise Exception("Array length should be at least one for min-max finder to work")
        if not isinstance(ints, list) or not all(isinstance(x, int) for x in ints):
            raise Exception("The parameter must be a list of integers")
        max_int = None
        min_int = None
        for index, i in enumerate(ints):
            if index == 0: # This is the first iteration
                max_int = min_int = i
            else:
                # Current element is more than the max value found o far
                if i > max_int:
                    max_int = i
                # Current value is less than the min value found so far
                elif i < min_int:
                    min_int = i
        return (min_int, max_int)


class TestSinglePassMinMaxFinder(unittest.TestCase):
    # The list contains only one element. Min & max values will be same
    def test_get_min_max_when_list_has_one_element_only(self):
        self.assertEqual(SinglePassMinMaxFinder.get_min_max([10]), (10, 10))

    # The list is empty. Min & max values will be (None, None)
    def test_get_min_max_when_list_is_empty(self):
        with self.assertRaises(Exception) as context:
            SinglePassMinMaxFinder.get_min_max([])
        self.assertTrue('Array length should be at least one for min-max finder to work' in str(context.exception))

    # The list is non-empty with more than 1 element
    def test_get_min_max_when_list_has_twenty_elements(self):
        l = [random.randint(0, 100) for i in range(0, 20)]  # a list containing 0 - 9
        random.shuffle(l)
        min_element = min(l)
        max_element = max(l)
        self.assertEqual(SinglePassMinMaxFinder.get_min_max(l), (min_element, max_element))

    def test_get_min_max_when_passed_int_instead_of_list_of_int(self):
        with self.assertRaises(Exception) as context:
            SinglePassMinMaxFinder.get_min_max(5)
        self.assertTrue('The parameter must be a list of integers' in str(context.exception))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSinglePassMinMaxFinder)
    unittest.TextTestRunner(verbosity=2).run(suite)