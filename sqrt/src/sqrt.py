"""
Class to implement square root function without using sqrt function in math library
"""
class Sqrt:
    """
    Parameter:
        number: number whose square root need to be calculated
    Returns:
        Floor value of the square root
    """
    # The square root lies between [1, number]
    # Initial guess is 1. If the square of the result computed is too far off from the given number then iterate
    # Iteration uses 0.5 * (start + number / start) as next guess
    # Iteration continues till convergence is achieved
    @staticmethod
    def sqrt(number, start=1.0):
        if number < 0:
            raise ValueError('Square root of a negative number can not be computed')
        while abs(start * start - number) > 0.1:
            start = (start + number / start) * 0.5
        return int(start)
