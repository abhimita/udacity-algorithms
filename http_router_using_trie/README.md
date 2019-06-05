# Introduction

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler

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

