# Introduction

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

## Directory organization

There are two directories. 
1. `src` - contains the source code
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=min_max/src python min_max/test/test_single_pass_min_max_finder.py`

### Output
```
test_get_min_max_when_list_has_one_element_only (__main__.TestSinglePassMinMaxFinder) ... ok
test_get_min_max_when_list_has_twenty_elements (__main__.TestSinglePassMinMaxFinder) ... ok
test_get_min_max_when_list_is_empty (__main__.TestSinglePassMinMaxFinder) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```


## Code design

The list of numbers is scanned. Two variables are used - one to hold the max value and other one to hold the min value. For every element in the list, a comparison is made whether the element is bigger(smaller) than the max(min) value seen so far. The variables are updated appropriately. This way the max & min values are determined in a single pass with time complexity O(n)
