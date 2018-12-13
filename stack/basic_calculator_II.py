import operator

class Solution:

    # @staticmethod
    def priority(self, char):
        if char == '*' or char == '/':
            return 3
        elif char == '+' or char == '-':
            return 2
        elif char == '(':
            return 1
        elif char == ')':
            return -1
        return None

    def postfix(self, input_array):
        result = list()
        stack = list()
        for item in input_array:
            op = self.priority(item)
            if op:
                if stack or op == -1:
                    print(stack)
                    if op == -1:
                        while True:
                            value = stack.pop(-1)
                            if self.priority(value) == 1:
                                break
                            result.append(value)
                    elif op == 1 or self.priority(stack[-1]) < op:
                        print('0 stack add', item)
                        stack.append(item)
                    elif self.priority(stack[-1]) >= op:
                        while True:
                            value = stack.pop(-1)
                            result.append(value)
                            if not stack or self.priority(stack[-1]) < op:
                                break
                        print('1 stack add', item)
                        stack.append(item)
                    else:
                        if item != '(' and item != ')':
                            result.append(item)
                else:
                    print('3 stack add', item)
                    stack.append(item)
            else:
                result.append(item)

        while stack:
            value = stack.pop(-1)
            result.append(value)
            # print(char, end='')
        return result

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        new_str = ''
        for char in s:
            if char == ' ':
                continue
            else:
                new_str += char

        s = new_str
        print(s)

        start = end = -1
        input = list()

        for index in range(len(s)):
            if self.priority(s[index]):
                end = index
                input.append(s[start:end])
                input.append(s[index])
                start = -1
                continue
            elif index == len(s)-1:
                end = index
                input.append(s[start:len(s)])
            elif start == -1:
                start = index

        print(input)

        result = self.postfix(input)
        print(result)

        stack = list()

        dict = {"+":operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

        for item in result:
            if self.priority(item):
                value1 = stack.pop(-1)
                value2 = stack.pop(-1)
                value = int(dict[item](value2, value1))
                print(value2, item, value1, '=', value)
                stack.append(value)
            else:
                stack.append(int(item))

        if stack:
            result = int(stack.pop(-1))
            print(result)
            return result


s = "(1+(4+5+2)-3)+(6+8)"
Sol = Solution()
Sol.calculate(s)