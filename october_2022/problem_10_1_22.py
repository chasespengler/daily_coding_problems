'''
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example:
[5, 3, '+']
should return
5 + 3 = 8

For example:
[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5 since
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5
'''
import operator

def reverse_polish(arr):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    # operators['+'](5, 3) = 8
    s = []
    for x in arr:
        if type(x) != str:
            s.append(x)
        else:
            two = s.pop()
            one = s.pop()
            s.append(operators[x](one, two))
    
    return s[0]

print(reverse_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))