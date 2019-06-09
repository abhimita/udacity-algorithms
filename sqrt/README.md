# Introduction

Here we compute the square root of a number without using Python's square root function in math library.

## Directory organization

There are two directories. 
1. `src` - contains the source code
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=sqrt/src python sqrt/test/test_sqrt.py`

As per Udacity project submission rubric test class is also copied into source file. So the following invocation will also work:

```PYTHONPATH=sqrt/src python sqrt/src/sqrt.py```

### Output
```
test_sqrt_for_perfect_square (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_negative (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_not_a_number (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_not_perfect_square (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_smallest_prime (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_zero (__main__.TestSqrt) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```


## Code design

We are using binary ssearch for finding the square root of the number. Our initial guess is `1` and square root of any number can't be more than half of the number. So the number will lie in the range [1, n/2]

Middle of the above range in n/4. For every guess, the square of the number is calculated and compared against the number. If it is less than tolerance level `0.01` then the iteration gets terminated. Otherwise, if square of the initial guess is less than the number, new range becomes [n/4, n/2] for search of square root of the number otherwise it becomes [1, n/4]

When the number is in [0,1] then it is handled separately.

### Time complexity

Since it is a binary search, range of search gets half in every iteration. Thus time complexity in O(logn)

### Space complexity

Other than storing few variables like `start`, `end`, `mid`, this logic doesn't require any additional storage. Thus space complexity is O(1)

