# Introduction

An array of integer is given. Two number need to be formed from array elements such that their sum is maximum. All array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. Python's sorting function can't be used and the expected time complexity should be O(nlog(n)).

## Directory organization

There are two directories. 
1. `src` - contains the source code
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=array_digits/src python array_digits/test/test_array_digits.py`

Test class is also copied into source file of the main class file as per Udacity rubic. So the following invocation also works:

```PYTHONPATH=search/src python array_digits/src/array_digits.py```

### Output
```
test_rearrange_digits_when_array_is_empty (__main__.TestArrayDigits) ... ok
test_rearrange_digits_when_even_number_of_elements (__main__.TestArrayDigits) ... ok
test_rearrange_digits_when_odd_number_of_elements (__main__.TestArrayDigits) ... ok
test_rearrange_digits_when_one_element_is_float (__main__.TestArrayDigits) ... ok
test_rearrange_digits_when_one_element_is_string (__main__.TestArrayDigits) ... ok
test_rearrange_digits_when_one_element_is_two_digited (__main__.TestArrayDigits) ... ok
test_rearrange_digits_with_one_element (__main__.TestArrayDigits) ... ok
test_rearrange_digits_with_two_elements (__main__.TestArrayDigits) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```


## Code design

In order to make highest sum, two generated numbers need to be the largest numbers obeying the given constraints. This implies that highest value digit should in loeading position for the number and this logic needs to be repeated for all place values for numbers from left to right.

It will be best to have the array sorted. As the problem states not to use Python's sort method, so `MergeSort` class implements merge sort algorithm. This algorithm will excute with complexity <a href="https://www.codecogs.com/eqnedit.php?latex=O(nlog_2{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(nlog_2{n})" title="O(nlog_2{n})" /></a>

Once the array is sorted in descending order, digits from the array is picked up one at a time. If there are odd number of digits that means that two numbers will differ by one digit. For odd number of digits, the highest digit is used in the leading position of the first number. After that we are left with even number of digits.

Each digits is pulled out from descending ordered array and used alternately in the remaining leading place values of first and second number. 

### Time Complexity

We are using merge sort to do the initial sort of array element. Mergesort will have time complexity of <a href="https://www.codecogs.com/eqnedit.php?latex=O(nlog_2{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(nlog_2{n})" title="O(nlog_2{n})" /></a> 

The subsequent loop will iterate for n times having time complexity O(n). Out of these two terms dominating term will come from merge sort hence complexity is <a href="https://www.codecogs.com/eqnedit.php?latex=O(nlog_2{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(nlog_2{n})" title="O(nlog_2{n})" /></a>

### Space complexity

Merge sort will require additional space of O(n). There is some need of constant space for loop variables, two numbers that get formed. Out of all these the dominating term in O(n). Overall space complexity in O(n)
