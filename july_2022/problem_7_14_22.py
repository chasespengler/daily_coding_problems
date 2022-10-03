'''
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
A 1 represents land and 0 represents water, so an island is a group of 1s 
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''
'''

NOT DONE NOT DONE NOT DONE NOT DONE NOT DONE NOT DONE

'''
def check(loc, mat):
    vects = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
    for vect in vects:
        try:
            if mat[loc[0] + vect[0]][loc[1] + vect[1]] == 1:
                return False
        except:
            continue
    
    return True

def islands(mat):
    num = 0
    for r in range(len(mat)):
        row = mat[r]
        for c in range(len(row)):
            isle = row[c]
            if isle == 0:
                continue
            else:
                if check((r, c), mat):
                    num += 1

    return num

maps = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]

print(islands(maps))