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

### Output
```
test_router_with_invalid_path (__main__.TestRouter) ... ok
test_router_with_url_having_trailing_slash (__main__.TestRouter) ... ok
test_router_with_url_not_found (__main__.TestRouter) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```


## Code design

Router functions are implemented by `Router` class. Router uses trie data structure. Trie data structure is implemented in `RouteTrie` class which uses `RouteTrieNode` for presentation of individual nodes of trie.

`RouteTrieNode`: Provides method to insert a path component as a child after checking that the path component doesn't exist already

`RouteTrie`:
- Initialization method create the trie root with "/" as every URL path starts with "/"
- Insert method allows adding path compoments into trie (given a full path). It traverses the path recursively and delegates the insertion work to class `TrieNode` when child node need to be created.
- Find method allows traversing the tree following the given path components

`Router`:
- `add_handler`: allows associating a handler to a new path which doesn't exist already
- `find`: returns the handler given the path

