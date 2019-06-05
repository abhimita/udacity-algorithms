# Introduction

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. Python's sorting functions should not be used.

## Directory organization

There are two directories. 
1. `src` - contains the source code
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=dutch_national_flag/src python dutch_national_flag/test/test_sorting_zero_one_two.py`

### Output
```
test_sort_already_sorted_array (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_array_starting_with_two_ending_with_one (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_array_starting_with_zero_ending_with_two (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_empty_array (__main__.TestZeroOneTwoSorter) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```


## Code design

