import random

class SinglePassMinMaxFinder:
    @staticmethod
    def get_min_max(ints):
        max_int = None
        min_int = None
        for index, i in enumerate(ints):
            if index == 0:
                max_int = min_int = i
            else:
                if i > max_int:
                    max_int = i
                if i < min_int:
                    min_int = i
        return (min_int, max_int)


if __name__ == '__main__':
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == SinglePassMinMaxFinder.get_min_max(l)) else "Fail")