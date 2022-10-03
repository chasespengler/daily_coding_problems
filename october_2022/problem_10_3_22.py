'''
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
'''

def smoller(arr):
    new_arr = []
    for i in range(len(arr)):
        z = 0
        for x in range(i, len(arr)):
            if arr[x] < arr[i]:
                z += 1

        new_arr.append(z)

    return new_arr

print(smoller([3, 4, 9, 6, 1]))