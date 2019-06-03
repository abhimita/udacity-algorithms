"""
Class that implements sorting of elements
"""
class ZeroOneTwoSorter:
    # Sort is a static method so there is no need to create an instance of the class
    @staticmethod
    def sort(array):
        # There are three pointers: zero_ptr, one_ptr & two_ptr
        # zero_ptr & one_ptr are initialized to the starting of the array
        # two_ptr points to end of the array
        zero_ptr = one_ptr = 0
        two_ptr = len(array) - 1
        # Elements between one_ptr & two_ptr can be of three types
        # element == 0, swap it with element pointed by zero_ptr . Advance both zero & one_ptr
        # element == 1, just advance one_ptr - no swapping is needed
        # element == 2, swap it with element pointed to by two_ptr. Advance two_ptr
        while one_ptr <= two_ptr:
            if array[one_ptr] == 0:
                array[zero_ptr], array[one_ptr] = array[one_ptr], array[zero_ptr]
                zero_ptr += 1
                one_ptr += 1
            elif array[one_ptr] == 1:
                one_ptr += 1
            else:
                array[one_ptr], array[two_ptr] = array[two_ptr], array[one_ptr]
                two_ptr -= 1
        return array
