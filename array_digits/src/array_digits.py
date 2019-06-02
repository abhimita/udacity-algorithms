class MergeSort:
    @staticmethod
    def sort(array):
        if len(array) > 1:
            mid = len(array) // 2
            first = array[:mid]
            second = array[mid:]
            MergeSort.sort(first)
            MergeSort.sort(second)
            MergeSort.merge(first, second, array)

    @staticmethod
    def merge(first, second, array):
        len_first = len(first)
        len_second = len(second)
        i = j = k = 0
        while i < len_first and j < len_second:
            if first[i] >= second[j]:
                array[k] = first[i]
                i += 1
            else:
                array[k] = second[j]
                j += 1
            k += 1
        while i < len_first:
            array[k] = first[i]
            i += 1
            k += 1
        while j < len_second:
            array[k] = second[j]
            k += 1
            j += 1

class ArrayDigits:
    @staticmethod
    def rearrange_digits(array):
        sz = len(array)
        MergeSort.sort(array)
        first = ''
        second = ''
        if sz % 2 != 0:
            first = str(array[0])
            start_index = 1
        else:
            start_index = 0
        for index, element in enumerate(array[start_index:]):
            if index % 2 == 0:
                first += str(element)
            else:
                second += str(element)
        return [int(first), int(second)]



