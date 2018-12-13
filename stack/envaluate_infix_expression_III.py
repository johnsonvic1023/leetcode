import math
import operator

"""
Infix expression: 1.5 + 2 - log( (4 + 4) * 2) / 3.5
1. Use two stack: operator, operand
2. Input number type: int, float
3. Define the priority of operator
4. Algorithm
   4.1 Scan the input string
   4.2 If operand stack is empty or input operator is "(", "log(" if ... push to the operator stack
   4.3 If the top of operator stack >= input operator
       4.3.1 Pop it and pop two operand stack
       4.3.2 Store the result of above calculation
       4.3.3 Push input operator to the stack
   4.4 Else if input operator is ")", do step 4.3 until find "(" or "log(" ...
   4.5 Finaly, Pop the operator and calculate it with operand stack until operator stack is empty
   4.6 Return the top value of operand stack
"""

operand_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "log(": math.log}


def priority(input):
    if input == "*" or input == "/":
        return 3
    if input == "+" or input == "-":
        return 2
    if input == "(" or input == ")" or input == "log(":
        return 1


def isfloat(input):
    return True if input.find('.') else False


def getvalue(input):
    return float(input) if isfloat(input) else int(input)


def calculate(input):
    operator_stack = list()
    operand_stack = list()
    for item in input:
        op = priority(item)
        if op:
            # operator
            if len(operator_stack) == 0 or item == "(" or item == "log(":
                operator_stack.append(item)
            else:
                if item == ")":
                    # handle (), log() ... case
                    while True:
                        if operator_stack and operator_stack[-1] != "(" and operator_stack[-1] != "log(":
                            op_temp = operator_stack.pop(-1)
                            if len(operand_stack) >= 2:
                                value2 = operand_stack.pop(-1)
                                value1 = operand_stack.pop(-1)
                                value = operand_dict[op_temp](value1, value2)
                                operand_stack.append(value)
                                print(value1, op_temp, value2, "=", value)
                            else:
                                return "invalid expression"
                        elif operator_stack[-1] == "(":
                            operator_stack.pop(-1)
                            break
                        elif operator_stack[-1] == "log(":
                            op_temp = operator_stack.pop(-1)
                            if len(operand_stack) >= 1:
                                value1 = operand_stack.pop(-1)
                                value = operand_dict[op_temp](value1)
                                print(op_temp, value1, ")=", value)
                                operand_stack.append(value)
                                break
                            else:
                                return "invalid expression"
                else:
                    # handle other cases
                    while True:
                        if operator_stack and priority(operator_stack[-1]) >= op:
                            op_temp = operator_stack.pop(-1)

                            if len(operand_stack) >= 2:
                                value2 = operand_stack.pop(-1)
                                value1 = operand_stack.pop(-1)
                                value = operand_dict[op_temp](value1, value2)
                                operand_stack.append(value)
                                print(value1, op_temp, value2, "=", value)
                            else:
                                return "invalid expression"
                        else:
                            operator_stack.append(item)
                            break

        else:
            # operand
            operand_stack.append(getvalue(item))

    while operator_stack:
        op_temp = operator_stack.pop(-1)
        if len(operand_stack) >= 2:
            value2 = operand_stack.pop(-1)
            value1 = operand_stack.pop(-1)
            value = operand_dict[op_temp](value1, value2)
            operand_stack.append(value)
            print(value1, op_temp, value2, "=", value)
        else:
            return "invalid expression"

    # Error handling
    if len(operand_stack) >= 2:
        return "invalid expression"

    return operand_stack[-1]


# Test above function
input_string = '1.5 + 2 - log( ( 4 + 4 ) * 2 ) / 3.5'
input_array = input_string.split(' ')
# print(input_array)
result = calculate(input_array)
print(result)

# Validation
input_string = '1.5 + 2 - math.log( (4 + 4) * 2) / 3.5'
result = eval(input_string)
print(result)

# Test invalid expression
input_string = '1.5 + )'
input_array = input_string.split(' ')
result = calculate(input_array)
print(result)