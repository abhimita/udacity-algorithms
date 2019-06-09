import unittest

"""
Class to implement square root function without using sqrt function in math library
"""
class Sqrt:
    """
    Parameter:
        number: integer number whose square root need to be calculated
    Returns:
        Floor value of the square root
    """
    # The square root lies between [1, number]
    # Initial guess is 1. If the square of the result computed is too far off from the given number then iterate
    # Iteration uses 0.5 * (start + number / start) as next guess
    # Iteration continues till convergence is achieved
    @staticmethod
    def sqrt(number, error=.01):
        if not isinstance(number, int):
            raise ValueError('The parameter (number) needs to be integer')
        if number < 0:
            raise ValueError('Square root of a negative number can not be computed')
        if number <= 1:
            return number
        # The square root of a number can't be bigger than half of the number
        start = 0
        end = number / 2
        while start <= end:
            mid = (start + end) / 2
            sqr = mid * mid
            # Terminate as long as difference between square of the estimate and the number is less than error
            if abs(sqr - number) <= error:
                break
            elif sqr < number:
                # If start & mid values are same then there is no adjustment
                # It can happen when number = 2
                if start == mid:
                    break
                # Move the estimate towards right
                start = mid
            else:
                # Move estimate towards left
                end = mid
        return int(mid)

# Unit tests merged with actual implementation as per Udacity guidelines
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