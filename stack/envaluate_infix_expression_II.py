import math
import operator

operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, \
                 "cos(": math.cos}


# define input type
def isfloat(input):
    return True if input.find('.') > -1 else False


def getvalue(input):
    return float(input) if isfloat(input) else int(input)


# define priority
def priority(input):
    if input == '*' or input == '/':
        return 3
    if input == '+' or input == '-':
        return 2
    if input == '(' or input == 'cos(' or input == ')':
        return 1


def calculate(input):
    operator_stack = list()
    operand_stack = list()
    for item in input:
        op = priority(item)
        if op is None:
            operand_stack.append(getvalue(item))
        else:
            if operator_stack:
                if item == '(' or item == 'cos(':
                    operator_stack.append(item)
                elif item == ')':
                    # handle cos() and () case
                    while operator_stack:
                        if operator_stack[-1] != '(' and operator_stack[-1] != 'cos(':
                            op_compare = operator_stack.pop(-1)
                            if len(operand_stack) >= 2:
                                value1 = operand_stack.pop(-1)
                                value2 = operand_stack.pop(-1)
                                value = operator_dict[op_compare](value2, value1)
                                operand_stack.append(value)
                                print(value2, op_compare, value1, '=', value)
                        elif operator_stack[-1] == '(':
                            operator_stack.pop(-1)
                            break
                        else:
                            op_compare = operator_stack.pop(-1)
                            if len(operand_stack) >= 1:
                                value1 = operand_stack.pop(-1)
                                value = operator_dict[op_compare](value1)
                                operand_stack.append(value)
                                print(op_compare, value1, ') =', value)
                            break

                else:
                    while True:
                        if operator_stack and op <= priority(operator_stack[-1]):
                            op_compare = operator_stack.pop(-1)
                            if len(operand_stack) >= 2:
                                value1 = operand_stack.pop(-1)
                                value2 = operand_stack.pop(-1)
                                value = operator_dict[op_compare](value2, value1)
                                operand_stack.append(value)
                                print(value2, op_compare, value1, '=', value)
                        else:
                            operator_stack.append(item)
                            break
            else:
                operator_stack.append(item)

    while operator_stack:
        op_compare = operator_stack.pop(-1)
        if len(operand_stack) >= 2:
            value1 = operand_stack.pop(-1)
            value2 = operand_stack.pop(-1)
            value = operator_dict[op_compare](value2, value1)
            print(value2, op_compare, value1, '=', value)
            operand_stack.append(value)

    result = operand_stack[-1]
    return result

input = '1.5+20-99/cos(2+3)'
input_array = list()

# input_str = '1.5 +'
# input_array = input_str.split(' ')
# print('input_array: ', input_array)
# result = calculate(input_array)
# print('test: ', result)
#
# # Test
# input_str = '1.5 + cos( 2 )'
# result = eval(input_str)
# print('eval: ', result)