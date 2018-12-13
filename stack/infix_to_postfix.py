import operator

"""
Infix to postfix

1. Use stack to store operator
2. Calculate postfix expression

"""

class Solution:
    def __init__(self):
        self.output = list()
        self.dict = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    def priority(self, input):
        if input == '*' or input == '/':
            return 3
        elif input == '+' or input == '-':
            return 2
        elif input == '(' or input == ')':
            return 1

    def printouput(self):
        output = ''
        for item in self.output:
            output += item

        print(output)

    def to_postfix(self, input):
        stack = list()
        for item in input:
            op = self.priority(item)
            if op:
                if len(stack) == 0 or item == '(':
                    stack.append(item)
                else:
                    if item == ')':
                        # handle () case
                        while True:
                            if stack and stack[-1] != '(':
                                self.output.append(stack.pop(-1))
                            else:
                                stack.pop(-1)
                                break
                    else:
                        # handle other cases
                        while True:
                            if stack and self.priority(stack[-1]) >= op:
                                self.output.append(stack.pop(-1))
                            else:
                                stack.append(item)
                                break
            else:
                self.output.append(item)

        while stack:
            self.output.append(stack.pop(-1))

    def calculate_postfix(self):
        stack = list()
        for item in self.output:
            op = self.priority(item)
            if op:
                if len(stack) >= 2:
                    value2 = stack.pop(-1)
                    value1 = stack.pop(-1)
                    value = self.dict[item](value1, value2)
                    print(value1, item, value2, "=", value)
                    stack.append(value)
                else:
                    return "invalid expression"
            else:
                stack.append(int(item))

# Test
input_string = '1+(2+3-4)*9'
Sol = Solution()
Sol.to_postfix(input_string)
Sol.printouput()
Sol.calculate_postfix()

# Validation
print(eval(input_string))