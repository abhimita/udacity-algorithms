## Represents a single node in the Trie
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []

    def insert(self, char):
        for c in self.children:
            if c.char == char:
                return c
        child = TrieNode(char)
        self.children.append(child)
        return child



## Add a child node in this Trie

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def _insert(self, word, start):
        for c in word:
            start = start.insert(c)

    def insert(self, word):
        start = self.root
        self._insert(word + '/', start)

    def _find(self, prefix, wo):
        pass

    def find(self, prefix):
        start = self.root
        for p in prefix:
            found = False
            for c in start.children:
                if c.char == p:
                    start = c
                    found = True
                    break
        result = []
        if not found:
            return result
        else:
            self.traverse(start, '', result)
            print([r[1:] for r in result])



    def traverse(self, start, word, result):
        if start is None:
            return
        word = word + (start.char if start.char not in ['/', '*'] else '')
        for c in start.children:
            self.traverse(c, word, result)
        if len(start.children) == 0:
            result.append(word)


## Find the Trie node that represents this prefix

if __name__ == "__main__":
    trie = Trie()
    trie.insert("hackathon")
    trie.insert("hack")
    trie.insert("hacky")
    trie.insert("hammer")
    # trie.insert("ab")
    # trie.insert("acf")
    # print(trie.root.char, [c.char for c in trie.root.children])
    # result = []
    # trie.traverse(trie.root, '', result)
    # print(result)

    trie.find('hac')