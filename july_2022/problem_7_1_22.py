'''
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''
from random import randint

def rand7():
    return randint(1, 7)

def rand5():
    num = rand7()
    while num > 5:
        num = rand7()

    return num

