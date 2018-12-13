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
    delete TrieNode
    """


# driver function
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()