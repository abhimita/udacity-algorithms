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

Test class is also copied into the main Python script. So the following invocation will also work.

```PYTHONPATH=dutch_national_flag/src python dutch_national_flag/src/sorting_zero_one_two.py```

### Output
```
test_sort_already_sorted_array (__main__.TestZeroOneTwoSorter) ... ok
test_sort_int_other_than_0_1_2 (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_array_starting_with_two_ending_with_one (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_array_starting_with_zero_ending_with_two (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_empty_array (__main__.TestZeroOneTwoSorter) ... ok
test_sort_with_string_as_element (__main__.TestZeroOneTwoSorter) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```


## Code design

Sorting of the elements need to be accomplished in O(n) time complexity. So we can't use standard sorting algorithms like heapsort or mergesort which will result in <a href="https://www.codecogs.com/eqnedit.php?latex=O(nlog_2n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(nlog_2n)" title="O(nlog_2n)" /></a>

We use three pointers.
1. One pointer that will point to the index having the last zero after the array is sorted
2. One pointer that will point to the index having the last 1 after the array is sorted

Two pointers described above point to starting of the unsorted array during initialization. The third pointer points to the end of the array.

For example

<pre>

+--+--+--+--+--+--+--+
|1 | 0| 2| 1| 0| 2| 0|
+--+--+--+--+--+--+--+
^ ^                 ^
0 1                 2

</pre>
During the iteration pointers `0` and `1` moves towards right while pointer `2` moves towards left. 

The first execution for the above situation pointer `1` is moved one place to the right and all other pointers remain in their position. 

<pre>

+--+--+--+--+--+--+--+
|1 | 0| 2| 1| 0| 2| 0|
+--+--+--+--+--+--+--+
^   ^               ^
0   1               2

</pre>

Now pointer `1` points to value `0` which should ideally be in the front of the list. So elements pointed by pointer `0` and pointer `1` are swapped with both pointer advancing one position to the right.

<pre>

+--+--+--+--+--+--+--+
|0 | 1| 2| 1| 0| 2| 0|
+--+--+--+--+--+--+--+
    ^ ^             ^
    0 1             2

</pre>

As pointer `1` now points to value `1` which no longer in the leading position of the list, pointer `1` is allowed to advance.

<pre>

+--+--+--+--+--+--+--+
|0 | 1| 2| 1| 0| 2| 0|
+--+--+--+--+--+--+--+
    ^   ^           ^
    0   1           2

</pre>

Next pointer `1` points to value `2` which should be towards the end of the list once sorting completes. To fulfill that objective, elements pointed by pointer `1` and pointer `2` are swapped, also pointer `2` is moved one position towards left.

<pre>

+--+--+--+--+--+--+--+
|0 | 1| 0| 1| 0| 2| 2|
+--+--+--+--+--+--+--+
    ^   ^        ^
    0   1        2

</pre>

As pointer `1` now points to value `0`, it needs to complete another swap with element pointed by pointer `0`. Also both pointers are advanced one position to the right. This shows one a complete scan of the list will result in all `0`s appearing in the front, all `2`s appearing at the end with `1`s in between.

<pre>

+--+--+--+--+--+--+--+
|0 | 0| 1| 1| 0| 2| 2|
+--+--+--+--+--+--+--+
        ^  ^      ^
        0  1     2
        
As a single pass is made of the elements of list, time complexity is O(n)

</pre>

### Time complexity

`1` pointer and `2` pointers start from two opposite ends of the array. `1` pointers moves towards left and `2` pointer moves towards right. Loop iteration continues till two pinters cross each other. That means every element of the array needs to be examined. Thus time complexity is O(n)

### Space complexity

The algorithm doesn't require any additional storage other than storage for 3 pointers. So space complexity is O(1)

