'''
You are given an N by M matrix of 0s and 1s. Starting from the top left corner, 
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0
'''

def pathfinder(m):
    n = [[0 for x in range(len(m[0]))] for y in range(len(m))]
    n[0][0] = 1
    ran = max(len(m), len(m[0]))
    y = 0
    for i in range(ran):
        if i < len(m):
            for x in range(len(m[0])):
                if m[y][x] == 0 and x != 0:
                    n[y][x] += n[y][x-1]
                elif m[y][x] == 1:
                    n[y][x] = 0
            x = i
            print(n[0])
            print(n[1])
            print(n[2])
            print(n[3])
            print(n[4])
            print()

        if i < len(m[0]):
            for y in range(len(m)):
                if m[y][x] == 0 and y != 0:
                    n[y][x] += n[y-1][x]
                elif m[y][x] == 1:
                    n[y][x] = 0
            y = i + 1
            print(n[0])
            print(n[1])
            print(n[2])
            print(n[3])
            print(n[4])
            print()

    return n[-1][-1]

pathfinder([[0,0,1],
            [0,0,1],
            [1,0,0],
            [0,0,0],
            [0,1,0]])

        



    

