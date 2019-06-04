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

### Output
```
test_sqrt_for_perfect_square (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_not_perfect_square (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_smallest_prime (__main__.TestSqrt) ... ok
test_sqrt_when_number_is_zero (__main__.TestSqrt) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```


## Code design

<a href="https://www.codecogs.com/eqnedit.php?latex=\sqrt_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sqrt_n" title="\sqrt_n" /></a> will be a number that lies between [1,n]. We start with initial guess of `1` for <a href="https://www.codecogs.com/eqnedit.php?latex=\sqrt_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sqrt_n" title="\sqrt_n" /></a> We iterate till the absolute difference between square of the solution reached so far and the number is more than `0.1`

### Why does it work?

<br>
Assume our initial guess is `g` and square(g) or `g * g` < n. 
<a href="https://www.codecogs.com/eqnedit.php?latex=g&space;*&space;g&space;$\leq$n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g&space;*&space;g&space;$\leq$n" title="g * g $\leq$n" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=g&space;$\leq$n/g" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g&space;$\leq$n/g" title="g $\leq$n/g" /></a>
