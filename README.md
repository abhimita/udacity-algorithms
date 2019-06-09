# Introduction

This repository contains Python based solutions for Udacity algorithms course

## Contents 

The repository contains six directories. These are:

**1. Square root of an integer (`sqrt`):**

We need to find the square root of a number with Python's math library. The floor value of the square root should be returned.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5. The expected time complexity is O(log(n))

**2. Search in a rotated sorted array (`search`):**

A sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

We need to search for a value. If found in the array return its index, otherwise return -1. There is no duplicate in the array and algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

**3. Rearrange array elements (`array_digits`):**

An array of integer is given. Two number need to be formed from array elements such that their sum is maximum. All array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. Python's sorting function can't be used and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, any one pair is returned.

**4. Dutch National flag problem (`dutch_national_flag`):**

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. Python's sorting functions should not be used.

**5. Auto complete using Trie (`trie`):**

Here we are using a trie data structure to autocomplete words as prefixes are typed in.

**6. Max and min in a unsorted array (`min_max`):**

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

**7. HTTP router using trie (`http_router_using_trie`):**

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler

