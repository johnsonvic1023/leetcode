# Take two stacks:
#
# operator stack { for operators and parentheses }.
# operand stack.
#
# Algorithm
# If character exists to be read:
# 1. If character is operand push on the operand stack,
#    if character is (, push on the operator stack.
# 2. Else if character is operator
#      1. While the top of the operator stack is
#         not of smaller precedence than this character.
#      2. Pop operator from operator stack.
#      3. Pop two operands (op1 and op2) from operand stack.
#      4. Store op1 op op2 on the operand stack back to 2.1.
# 3. Else if character is ), do the same as 2.2 - 2.4 till you encounter (.
# 4. Else (no more character left to read):
#      1. Pop operators untill operator stack is not empty.
#      2. Pop top 2 operands and push op1 op op2 on the operand stack.
# 5. return the top value from operand stack.

import operator


class Solution:
    def priority(self, input):
        if input == '*' or input == '/':
            return 3
        elif input == '+' or input == '-':
            return 2
        elif input == '(' or input == ')':
            return 1

    def calculate(self, s):

        input = list()
        start = -1
        for index in range(len(s)):
            if self.priority(s[index]):
                if start != -1:
                    input.append(s[start:index])
                    start = -1
                input.append(s[index])
            elif index == len(s) - 1:
                input.append(s[start:len(s)])
                start = -1
            elif start == -1:
                start = index

        print(input)

        operator_stack = list()
        operand_stack = list()

        dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        for item in input:
            op = self.priority(item)
            if op:
                if item == '(':
                    operator_stack.append(item)
                elif operator_stack:
                    if item == ')':
                        while True:
                            if operator_stack[-1] != '(':
                                op_temp = operator_stack.pop(-1)
                                if len(operand_stack) >= 2:
                                    value1 = operand_stack.pop(-1)
                                    value2 = operand_stack.pop(-1)
                                    value = dict[op_temp](value2, value1)
                                    print(value1, op_temp, value2, value)
                                    operand_stack.append(int(value))
                            else:
                                operator_stack.pop(-1)
                                break
                    else:
                        while True:
                            if operator_stack and self.priority(operator_stack[-1]) >= op:
                                op_temp = operator_stack.pop(-1)
                                if len(operand_stack) >= 2:
                                    value1 = operand_stack.pop(-1)
                                    value2 = operand_stack.pop(-1)
                                    value = dict[op_temp](value2, value1)
                                    print(value1, op_temp, value2, value)
                                    operand_stack.append(int(value))
                            else:
                                operator_stack.append(item)
                                break
                else:
                    operator_stack.append(item)
            else:
                operand_stack.append(int(item))

        while operator_stack:
            op_temp = operator_stack.pop(-1)
            if len(operand_stack) >= 2:
                value1 = operand_stack.pop(-1)
                value2 = operand_stack.pop(-1)
                value = dict[op_temp](value2, value1)
                operand_stack.append(int(value))

        result = operand_stack[-1]
        print(result)
        return result


s = "(1+(4+5+2)-3)+(6+8)"
Sol = Solution()
Sol.calculate(s)

