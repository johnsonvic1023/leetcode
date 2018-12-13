"""
Use Trie
The Trie stores {"abc", "abcd", "aa", "abbbaba"}
User types in "ab"
The system should print {"abc", "abcd", "abbbbba"}

Algorithm
Insert and search in O(K), K is the length of key

Search for given query using standard Trie search algorithm.
If query prefix itself is not present, return -1 to indicate the same.
If query is present and is end of word in Trie, print query. This can quickly checked by seeing if last matching node has isEndWord flag set. We use this flag in Trie to mark end of word nodes for purpose of searching.
If last matching node of query has no children, return.
Else recursively print all nodes under subtree of last matching node.
"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def isLastNode(self):
        for c in self.children:
            if c:
                return False
        return True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        curr = self.root
        for char in key:
            index = self._charToIndex(char)
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]

        curr.isWord = True

    def search(self, key):
        curr = self.root
        for char in key:
            index = self._charToIndex(char)
            if curr.children[index]:
                curr = curr.children[index]
            else:
                return False
        return curr and curr.isWord

    """
    1. make sure current string is in Trie
    2. Recursive function to print auto-suggestions
    """

    def autoSuggestion(self, root, prefix):
        if root.isWord:
            print(prefix)

        if root.isLastNode():
            return

        for i in range(26):
            if root.children[i]:
                curr_prefix = prefix + chr(ord('a') + i)
                self.autoSuggestion(root.children[i], curr_prefix)

    def printAutoSuggestions(self, query):
        curr = self.root

        index = -1
        for i in range(len(query)):
            index = self._charToIndex(query[i])
            if curr.children[index]:
                curr = curr.children[index]
            else:
                print("No other strings found with this prefix")
                return

        if curr and curr.isWord and curr.isLastNode():
            print("No other strings to suggest")
            return

        if not curr.isLastNode():
            self.autoSuggestion(curr, query)



# Insert test case
trie = Trie()
keys = ["hello", "dog", "hell", "cat", "a", "hel", "help", "helps", "helping"]
for key in keys:
    trie.insert(key)

trie.printAutoSuggestions("hel")