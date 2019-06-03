import math
class Sqrt:
    @staticmethod
    def sqrt(number, start=1.0):
        while abs(start * start - number) > 0.1:
            start = (start + number / start) * 0.5
        return math.floor(start)

if __name__ == '__main__':
    print(Sqrt.sqrt(25))