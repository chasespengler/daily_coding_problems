'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

#First attempt with using division
array = [1, 2, 3, 4, 5]
product = 1
new_array_1 = []
for i in array:
    product = product * i
for i in array:
    new_array_1.append(product / i)

print(new_array_1)

#Second attempt without division
new_array_2 = []
for i in range(len(array)):
    arr_1 = array[:i]
    arr_2 = array[i + 1:]
    arr_3 = arr_1 + arr_2
    product = 1
    for x in arr_3:
        product = product * x

    new_array_2.append(product)

print(new_array_2)
    