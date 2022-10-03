'''
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def lowest_int(arr):
    arr.sort()
    print(arr)
    if arr[0] > 1 or arr[-1] <= 0:
        return 1
    for i in range(1, len(arr)):
        num1 = arr[i - 1]
        num2 = arr[i]
        if num2 > 0 and num1 >= 0 and num2 - num1 > 1:
            return num1 + 1
    return num2 + 1

arr = [3, 4, -1, 1]
arr2 = [1, 2, 0]
arr3 = [-1000, -100, -10, -87, -69, -400]
print(lowest_int(arr))
print(lowest_int(arr2))
print(lowest_int(arr3))

