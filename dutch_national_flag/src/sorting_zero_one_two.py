
class ZeroOneTwoSorter:
    @staticmethod
    def sort(array):
        zero_ptr = one_ptr = 0
        two_ptr = len(array) - 1
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

if __name__ == '__main__':
    print(ZeroOneTwoSorter.sort([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))