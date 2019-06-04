from sqrt import Sqrt
import unittest

class TestSqrt(unittest.TestCase):
    # Test when input number is perfect square
    def test_sqrt_for_perfect_square(self):
        self.assertEqual("Pass" if (5 == Sqrt.sqrt(25)) else "Fail", "Pass")
    # Test when input number is not perfect square
    def test_sqrt_when_number_is_not_perfect_square(self):
        self.assertEqual("Pass" if (5 == Sqrt.sqrt(27)) else "Fail", "Pass")
    # Test when input number is zero
    def test_sqrt_when_number_is_zero(self):
        self.assertEqual("Pass" if  (0 == Sqrt.sqrt(0)) else "Fail", "Pass")
    def test_sqrt_when_number_is_smallest_prime(self):
        self.assertEqual("Pass" if  (1 == Sqrt.sqrt(2)) else "Fail", "Pass")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSqrt)
    unittest.TextTestRunner(verbosity=2).run(suite)