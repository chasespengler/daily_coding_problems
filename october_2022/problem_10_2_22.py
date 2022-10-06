'''
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
'''

def pigeonhole(arr, myset):
    for x in arr:
        if x in myset:
            myset.remove(x)
        else:
            return x

x = {1, 2, 3, 4, 4}
y = [1, 2, 3, 4, 4]

print(pigeonhole(y, x))