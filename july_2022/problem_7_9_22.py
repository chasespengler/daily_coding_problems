'''
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
'''

def non_dec(arr):
    one_mod = False
    for i in range(1, len(arr)):
        first = arr[i-1]
        second = arr[i]
        if first > second:
            if one_mod:
                return False
            one_mod = True
        
    return True

print(non_dec([10, 5, 7]))
print(non_dec([10, 5, 1]))
print(non_dec([10, 9, 5]))
