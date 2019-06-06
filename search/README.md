# Introduction

A sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

We need to search for a value. If found in the array return its index, otherwise return -1. There is no duplicate in the array and algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
## Directory organization

There are two directories. 
1. `src` - contains the source code
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=search/src python search/test/test_search_rotated_array.py`

### Output
```
test_search_rotated_array_for_max_element_when_list_has_non_contiguous_numbers (__main__.TestSearchRotatedArray) ... ok
test_search_rotated_array_for_min_element_when_list_has_non_contiguous_numbers (__main__.TestSearchRotatedArray) ... ok
test_search_rotated_array_for_number_not_present (__main__.TestSearchRotatedArray) ... ok
test_search_rotated_array_pivot_point_is_at_the_start (__main__.TestSearchRotatedArray) ... ok
test_search_rotated_array_when_min_element_is_near_middle (__main__.TestSearchRotatedArray) ... ok
test_search_rotated_array_when_search_element_is_in_first_position (__main__.TestSearchRotatedArray) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## Code design

This is a modified version of binary search. Normal binary search will let us find the presence or absence of an element in sorted array in <a href="https://www.codecogs.com/eqnedit.php?latex=O(log_2n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(log_2n)" title="O(log_2n)" /></a>

In this problem the sorted array is pivoted at a point. The first step is to find the pivot point. Numbers to the left of pivot point remains sorted in ascending order. Same is true for the numbers to the right of the pivot point. In the above example the pivot point is where element 7 is located.

`find_max_index` determines the pivot point. It handles the special case of when the list has one or two elements. Both of which are trivial. When the list is having more than 2 elements then the middle element of the list is accessed. If it is more than the element to its left and to its right, then that is the maximum value in the list.

Otherwise if the element at `index = 0` is greater than element at `index = mid` then the maximum value need to the search to the left of the middle index. Right portion should be search if the reverse is true. The same routine is called recursively after adjusting left (right) index indicating whether right(left) of the array is searched. Just like binary search size of the array gets decreased by factor 2. Thus the time complexity is <a href="https://www.codecogs.com/eqnedit.php?latex=O(log_2n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(log_2n)" title="O(log_2n)" /></a>

Once the position of maximum value is known binary search is used to determine the absence or presence of the given element by comparing the value of the given element with that of element at `index=0` and the element at `index = pivot point - 1`. If the element falls within the range, then binary search can be used here as this segment of the array is sorted.

Otherwise binary search can be used for segment of the array between `index = pivot point + 1` and end of the array. So the overall time complexity is <a href="https://www.codecogs.com/eqnedit.php?latex=O(log_2n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(log_2n)" title="O(log_2n)" /></a>
