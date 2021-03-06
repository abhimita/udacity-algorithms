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

    # Test when input is smallest prime (2)
    def test_sqrt_when_number_is_smallest_prime(self):
        self.assertEqual("Pass" if  (1 == Sqrt.sqrt(2)) else "Fail", "Pass")

    # Test when input is negative. Should throw exception
    def test_sqrt_when_number_is_negative(self):
        with self.assertRaises(Exception) as context:
            Sqrt.sqrt(-25)
        self.assertTrue('Square root of a negative number can not be computed' in str(context.exception))

    # Test when input is not a number. Should throw exception
    def test_sqrt_when_number_is_not_a_number(self):
        with self.assertRaises(Exception) as context:
            Sqrt.sqrt('a')
        self.assertTrue('The parameter (number) needs to be integer' in str(context.exception))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSqrt)
    unittest.TextTestRunner(verbosity=2).run(suite)