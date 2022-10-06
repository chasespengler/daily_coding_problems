'''
Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.

has_next(): returns whether or not the iterator still has elements left

'''

class iterator:
    def __init__(self, arr):
        self.arr = arr
        self.i = 0
        self.y = 0
        self.init = True

    def next(self):
        if self.init:
            self.init = False
            return self.arr[0][0]
        if self.has_next():
            return self.arr[self.i][self.y]
        else:
            raise Exception("No more numbers")

    def has_next(self):
        if self.y != len(self.arr[self.i]) - 1:
            self.y += 1
            return True
        elif self.i != len(self.arr) - 1:
            self.i += 1
            self.y = 0
            return True
        else:
            return False

my = iterator([[1, 2], [3], [4, 5, 6], [7]])

print(my.next())
print(my.next())
print(my.next())
print(my.next())
print(my.next())
print(my.next())
print(my.next())
print(my.next())
print(my.next())