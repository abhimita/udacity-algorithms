"""
Implements Merge sort. Sorting is done in-place.
"""
class MergeSort:
    """
    Parameters:
        array: Array to be sort
    """
    @staticmethod
    # Recursive method for merge sort
    def sort(array):
        # Sorting is needed only when array contains more than one element
        if len(array) > 1:
            # Determine mid of the array
            mid = len(array) // 2
            first = array[:mid]
            second = array[mid:]
            # Recursively call merge sort for the first half of the array
            MergeSort.sort(first)
            # Recursively call merge sort for second half of the array
            MergeSort.sort(second)
            # Merge two sorted arrays
            MergeSort.merge(first, second, array)

    """
    Merges two sorted arrays. Final array is sorted in descending order
    Parameters:
        first: First array
        second: Second array
        array: Array containing descending sorted numbers   
    """
    @staticmethod
    def merge(first, second, array):
        len_first = len(first)
        len_second = len(second)
        i = j = k = 0
        while i < len_first and j < len_second:
            # Descending sort
            # Pick up elements from first array when the element is greater
            # than the current element in second array
            if first[i] >= second[j]:
                array[k] = first[i]
                i += 1
            else:
                # Pick up element from second array
                array[k] = second[j]
                j += 1
            k += 1
        # Pick up any residual elements form first array which didn't make it to final array
        while i < len_first:
            array[k] = first[i]
            i += 1
            k += 1
        # Pick up any residual elements form second array which didn't make it to final array
        while j < len_second:
            array[k] = second[j]
            k += 1
            j += 1

"""
Class that solves the problem of generating two numbers from initegers in the array
so that the sum of the two number is maximum obeying the constraints listed in the problem
"""
class ArrayDigits:
    """
    Parameters:
        array: Array containing the digits from which two numbers need to be formed
    """
    @staticmethod
    def rearrange_digits(array):
        sz = len(array)
        if sz <= 1:
            raise Exception("Array length is no sufficient to return two numbers")
        # Sort the array in descending order
        MergeSort.sort(array)
        first = ''
        second = ''
        # If the array contains odd number of integers then one of the two numbers
        # will have one extra digit position compared to the other one
        if sz % 2 != 0:
            # Pick up the largest integer for the leading digit of the first number
            first = str(array[0])
            start_index = 1
        else:
            start_index = 0
        # Highest values pulled out from descending sorted array
        # Alternate these integers to be used in consecutive leading place
        # values for first and second numbers with place values being filled
        # from left to right
        for index, element in enumerate(array[start_index:]):
            if index % 2 == 0:
                first += str(element)
            else:
                second += str(element)
        return [int(first), int(second)]
