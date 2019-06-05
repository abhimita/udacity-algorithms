# Introduction

An array of integer is given. Two number need to be formed from array elements such that their sum is maximum. All array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. Python's sorting function can't be used and the expected time complexity is O(nlog(n)).

## Directory organization

There are two directories. 
1. `src` - contains the source code
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=array_digits/src python array_digits/test/test_array_digits.py`

### Output
```
test_rearrange_digits_when_even_number_of_elements (__main__.TestArrayDigits) ... ok
test_rearrange_digits_when_odd_number_of_elements (__main__.TestArrayDigits) ... ok
test_rearrange_digits_with_one_element (__main__.TestArrayDigits) ... ok
test_rearrange_digits_with_two_elements (__main__.TestArrayDigits) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```


## Code design

In order to make highest sum, the generated numbers need to be the largest numbers obeying the given constraints. This implies that highest value digit need to be used in highest place value position for the number and this logic needs to be repeated for lower place values with numbers being formed from left to right.

It will be best to have the array sorted. As the problem states not to be Python's sort method, so `MergeSort` class implements merge sort algorithm. This algorithm will excute with complexity <a href="https://www.codecogs.com/eqnedit.php?latex=O(nlog_2{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(nlog_2{n})" title="O(nlog_2{n})" /></a>

One the array is sorted in descending order, digits from the array is picked up one at a time. If there are odd number of digits that means that two numbers will differ by one digit. For odd number of digits, the highest digit is used in the leading position of the first number. After that we are left with even number of digits.

Each digits is pulled out from descending ordered array and used in the remaining leading place values of first and second number. This loop will get executed O(n) times. The dominating term will be the complexity of merge sort.
