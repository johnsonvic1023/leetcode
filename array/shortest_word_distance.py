import collections

"""
Shortest Word Distance

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3. Given word1 = "makes", word2 = "coding", return 1.
"""


class Solution:
    def distance(self, input, word1, word2):
        dict = collections.defaultdict(list)
        for index in range(len(input)):
            dict[input[index]].append(index)

        print(dict)

        list1 = dict[word1] if word1 in dict else []
        list2 = dict[word2] if word2 in dict else []

        print(list1, list2)

        """
        Smallest Difference pair of values between two sorted Arrays
        """
        min = float('inf')
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if min >= abs(list1[i] - list2[j]):
                min = abs(list1[i] - list2[j])
            if list1[i] >= list2[j]:
                j += 1
            else:
                i += 1
        print(min)


input = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
Sol = Solution()
Sol.distance(input, word1, word2)