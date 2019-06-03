from sqrt import Sqrt
import unittest

class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual("Pass" if (5 == Sqrt.sqrt(25)) else "Fail", "Pass")
        self.assertEqual("Pass" if (5 == Sqrt.sqrt(27)) else "Fail", "Pass")
        self.assertEqual("Pass" if (4 == Sqrt.sqrt(16)) else "Fail", "Pass")
        self.assertEqual("Pass" if  (0 == Sqrt.sqrt(0)) else "Fail", "Pass")
        self.assertEqual("Pass" if  (3 == Sqrt.sqrt(9)) else "Fail", "Pass")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSqrt)
    unittest.TextTestRunner(verbosity=2).run(suite)