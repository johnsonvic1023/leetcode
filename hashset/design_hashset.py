class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.bucket_set = [[] for _ in range(self.size)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            return

        value = self.hash_function(key)
        bucket = self.bucket_set[value]
        bucket.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            value = self.hash_function(key)
            bucket = self.bucket_set[value]
            index = self.item_index(key)
            bucket.pop(index)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.item_index(key) != -1

    def hash_function(self, key):
        return key % self.size

    def item_index(self, key):
        value = self.hash_function(key)
        bucket = self.bucket_set[value]
        for index, item in enumerate(bucket):
            if item == key:
                return index
            elif index == len(bucket) - 1:
                return -1
        return -1


# Test case
obj = MyHashSet()
obj.add(3)
obj.add(10)
obj.remove(3)
result = obj.contains(10)
print(result)