'''
Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
'''

def hopper(arr):
    ind = 0
    while ind < len(arr):
        if ind == len(arr)-1:
            return True
        loc = arr[ind]
        if loc == 0:
            return False
        ind += loc

    return True

z = [2, 0, 1, 0]
a = [1, 1, 0, 1]
print(hopper(z))
print(hopper(a))
