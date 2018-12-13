class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.hash_map[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """

        for item in self.hash_map.keys():
            if key == item:
                return self.hash_map[key]
        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if self.get(key) != -1:
            del self.hash_map[key]


obj = MyHashMap()
obj.put(2,1)
result = obj.get(2)
print(result)
obj.put(2,2)
obj.remove(3)
result = obj.get(2)
print(result)