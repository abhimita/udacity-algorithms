class SearchRotatedArray:
    @staticmethod
    def rotated_array_search(input_list, number):
        max_index = SearchRotatedArray.find_max_index(input_list, 0, len(input_list) - 1)
        if input_list[max_index] == number:
            return max_index
        elif input_list[max_index] < number:
            return -1
        else:
            if number < input_list[max_index - 1] and input_list[0] <= number:
                return SearchRotatedArray.ascending_binary_search(input_list, 0, max_index - 1, number)
            else:
                return SearchRotatedArray.ascending_binary_search(input_list, max_index + 1, len(input_list) - 1, number)

    @staticmethod
    def ascending_binary_search(input_list, left, right, number):
        if left > right:
            return -1
        else:
            mid = int((left + right) / 2)
            if input_list[mid] == number:
                return mid
            elif input_list[mid] >= number:
                return SearchRotatedArray.ascending_binary_search(input_list, left, mid, number)
            else:
                return SearchRotatedArray.ascending_binary_search(input_list, mid + 1, right, number)

    @staticmethod
    def find_max_index(input_list, left, right):
        if left > right: \
                return -1
        else:
            if left == right:
                return left
            elif left + 1 == right:
                return left if input_list[left] >= input_list[left + 1] else left + 1
            else:
                mid = int((left + right) / 2)
                if input_list[mid] > input_list[mid - 1] and input_list[mid] > input_list[mid + 1]:
                    return mid
                elif input_list[mid - 1] > input_list[mid] and input_list[mid] < input_list[mid + 1]:
                    return mid - 1
                elif input_list[mid] < input_list[mid - 1] and input_list[mid + 1] < input_list[mid]:
                    return SearchRotatedArray.find_max_index(input_list, left, mid - 1)
                else:
                    return SearchRotatedArray.find_max_index(input_list, mid + 1, right)

    @staticmethod
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

if __name__ == '__main__':
    print(SearchRotatedArray.rotated_array_search([6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4], 2))
