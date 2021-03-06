'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''

mat = \
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25]]

def spiral1(mat):
    up = False
    right = True
    cmax = len(mat[0])
    rmax = len(mat)
    cmin = 0
    rmin = 1
    r = 0
    i = 0

    while i < len(mat) * len(mat[0]):
        if right:
            for c in range(cmin, cmax, 1):
                #print("r", r, c)
                print(mat[r][c])
                i += 1
            right = not right
            cmax -= 1
        if not up:
            for r in range(rmin, rmax, 1):
                #print("d", r, c)
                print(mat[r][c])
                i += 1
            up = not up
            rmax -= 1
        if not right:
            for c in range(cmax-1, cmin-1, -1):
                #print("l", r, c)
                print(mat[r][c])
                i += 1
            right = not right
            cmin += 1
        if up:
            for r in range(rmax-1, rmin-1, -1):
                #print("u", r, c)
                print(mat[r][c])
                i += 1
            up = not up
            rmin += 1

def next_vect(vects):
    new_vects = vects[1:]
    new_vects.append(vects[0])
    return new_vects

#Not functional
def spiral(mat):     
    printed_mat = []
    vects = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    r = 0
    c = 0
    print("work")
    for i in range(len(mat) * len(mat[0])):
        print(r, c)
        if mat[r][c] not in printed_mat:
            if r < len(mat) and c < len(mat[0]) - 1:
                r += vects[0][1]
                c += vects[0][0]
            else:
                print(vects[0])
                vects = next_vect(vects)
                print(vects[0])
                r += vects[0][1]
                c += vects[0][0]

spiral1(mat)

# vects = [[0, 1], [1, 0], [0, -1], [1, 0]]
# rmax = len(mat) - 1
# cmax = len(mat[0]) - 1
# cmin = 0
# rmin = 0
# r = 0
# c = 0
# toggle = True
# for vect in vects:
#     if toggle:
#         while cmin <= c < cmax:
#             print(mat[r][c])
#             r += vect[0]
#             c += vect[1]

#         toggle = not toggle
#         print("switch ", r, " ", c)
#     else:
#         while rmin < r <= rmax:
#             print(mat[r][c])
#             r += vect[0]
#             c += vect[1]

#         toggle = not toggle
#         print("switch ", r, " ", c)
#         r -= 1
#         c -= 1       

        