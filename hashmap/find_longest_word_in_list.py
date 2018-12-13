"""
Design algorithm to find the longest word in list, the substring of this word should also in list
For example:
1. list = {"super", "man", "aasuperman", "superman"}, longest word is "superman"
2. list = {"super", "man", "aasuperman", "aa", "superman"}, longest word is "aasuperman"
3. list = {"super," "man"}, longest word is ''

Algorithm
1. Use hash table
2. Use Recursive
"""


def find_longest(input_list, item, i, j):
    if item[i:j] in input_list:
        return True
    elif j - i > 1:
        for index in range(i+1, j-i-1):
            left_result = find_longest(input_list, item, i, index)
            right_result = find_longest(input_list, item, index, j)
            if left_result and right_result:
                return True
    else:
        return False


def print_longest_word(input_list):
    longest_word = ''
    longest = 0
    for item in input_list:
        for index in range(1, len(item)-1):
            left_result = find_longest(input_list, item, 0, index)
            right_result = find_longest(input_list, item, index, len(item))
            # print("Test: ", item[0:index], item[index:len(item)])
            # print("left_result: ", left_result)
            # print("right_result: ", right_result)
            if left_result and right_result and longest <= len(item):
                longest = len(item)
                longest_word = item
                break
    print("longest_word:", longest_word)


# Test
list = ['super', 'man', 'aasuperman', 'aa', 'superman']
list.sort(key=len, reverse=True)
print(list)

print_longest_word(list)


