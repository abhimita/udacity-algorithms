# Introduction

Here we are using a trie data structure to autocomplete words as prefixes are typed in

## Directory organization

There are one directory which contains the python notebook. 
1. `src` - contains the source code


## Code design

The implementation consists of two classes

1. `TrieNode`: This class offers two methods.
  - `insert` : allows insertion of a child node to this node if the character is not in a child node alreadt
  - `suffixes` : A recursive routine to get all suffixes with respect to this node. This method is invoked as prefix characters are typed.
  
2. `Trie`: This class offers two methods
  - `insert`: inserts a word to trie
  - `find`: Find the Trie node that represents this prefix
  
### Time Complexity

In trie data structure we are performing two types of operations.

1. Insertion - Assume that there are W words in the list and average length of word in L. So to create the trie time complexity in O(W * L)

2. Find - As insertion of new word always precedes finding so time complexity for finding also O(W * L)

### Space Complexity

Space complexity can be derived by examining number of nodes in trie. Number of nodes will vary depending on number of prefixes in comoon within th egiven word list.

Let us assume best case scenario. Word list is ['abc', 'abd', 'abe', 'abf'] This will result in a trie having 7 nodes (including root node). Here each word has same prefix except the last character position. W * 1.5 + 1 where W = 4

Example of worst case scenario will be ['abc', 'def', 'ghi', 'xyz']. This trie will have 13 nodes (W * 3 + 1) where W = 4

This space complexity in O(W * L)
