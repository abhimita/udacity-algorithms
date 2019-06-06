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
