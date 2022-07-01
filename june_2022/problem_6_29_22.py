'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''
from re import A


arr = [-10, -10, 5, 2, 17, -20]

def largest_prod(arr):
    arr.sort()
    z = arr[0] * arr[1] * arr[-1]
    a = arr[-3] * arr[-2] * arr[-1]
    if a >= z:
        return a 
    else:
        return z

print(largest_prod(arr))

    
