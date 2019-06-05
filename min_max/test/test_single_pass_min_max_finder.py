import unittest
from single_pass_min_max_finder import SinglePassMinMaxFinder
import random

class TestSinglePassMinMaxFinder(unittest.TestCase):
    # The list contains only one element. Min & max values will be same
    def test_get_min_max_when_list_has_one_element_only(self):
        self.assertEqual(SinglePassMinMaxFinder.get_min_max([10]), (10, 10))

    # The list is empty. Min & max values will be (None, None)
    def test_get_min_max_when_list_is_empty(self):
        self.assertEqual(SinglePassMinMaxFinder.get_min_max([]), (None, None))

    # The list is non-empty with more than 1 element
    def test_get_min_max_when_list_has_twenty_elements(self):
        l = [random.randint(0, 100) for i in range(0, 20)]  # a list containing 0 - 9
        random.shuffle(l)
        min_element = min(l)
        max_element = max(l)
        self.assertEqual(SinglePassMinMaxFinder.get_min_max(l), (min_element, max_element))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSinglePassMinMaxFinder)
    unittest.TextTestRunner(verbosity=2).run(suite)