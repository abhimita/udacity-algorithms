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
2. `PYTHONPATH=http_router_using_trie/src python http_router_using_trie/test/test_router.py`

Test class is also copied into the source file as per Udacity submission rubric. So the following invocation will also work:

```PYTHONPATH=http_router_using_trie/src python http_router_using_trie/src/router.py```

### Output
```
test_router_with_invalid_path (__main__.TestRouter) ... ok
test_router_with_url_having_trailing_slash (__main__.TestRouter) ... ok
test_router_with_url_not_found (__main__.TestRouter) ... ok
test_router_with_url_not_having_trailing_slash (__main__.TestRouter) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```


## Code design

There are three classes in the implementation.

1. `RouterTrieNode`
2. `RouterTrie`
3. `Router`

`RouteTrieNode`: Provides template for the node in a trie. It defines the instance variables that consists of (1) `value` (2) `handler` and (3) `children`

This class provides method to insert a path component as a child after checking that the path component doesn't already exist.

URL specified as `/a/b/c` is defined to have 3 path components `a`, `b` & `c` and a special node `/` (root node)

`RouterTrie`: Provides template for trie.

This class provides 
- Initialization method create the trie root with "/" as every URL path starts with "/"
- Insert method allows adding path compoments into trie (given a full path). It traverses the path recursively and delegates the insertion work to class `TrieNode` when child node need to be created.
- Find method allows traversing the tree following the given path components and returns a handler to the node

`Router`: Router is the top level class that uses trie data structure. 

- `add_handler`: allows associating a handler to a new path if doesn't exist already
- `lookup`: returns the handler given the path

### Time complexity

Assume that there are W URLs are used in `add_handler` method. For every URL on an average `L` components are there. `add_handler` or `lookup` will have O(W * L) time complexity. 

### Space complexity

Space complexity is O(W * L) as well.
