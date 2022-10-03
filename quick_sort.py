myarr = [1, 5, 0, 7, 11, 26, 13, 12, 22, 3]
from random import randint

def quick(arr):
    part = arr.pop(-1)
    left = []
    right = []

    for x in arr:
        if x <= part:
            left.append(x)
        else:
            right.append(x)

    myarr[len(left)-1] = part
    while left:
        quick(left)
    #if right:
        #quick(right)

quick(myarr)

print(myarr)