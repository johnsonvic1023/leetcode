class TrieNode:
    def __init__(self):
        self.child = dict()
        self.isWord = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            child = curr.child.get(char)
            if child is None:
                child = TrieNode()
                curr.child[char] = child
            curr = child
        curr.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            child = curr.child.get(char)
            if child is None:
                return False
            curr = child
        return curr.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            child = curr.child.get(char)
            if child is None:
                return False
            curr = child
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
result = obj.search("apple")
print(result)
result = obj.search("app")
print(result)
result = obj.startsWith("app")
print(result)
obj.insert("app")
result = obj.search("app")
print(result)