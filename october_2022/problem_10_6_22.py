'''
Given an N by N matrix, rotate it by 90 degrees clockwise

eg

[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

->

[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
'''

def rotate(arr):
    n = len(arr)
    new_arr = []
    for c in range(n):
        new_row = []
        for r in range(n):
            new_row.append(arr[-1-r][c])

        new_arr.append(new_row)
    
    return new_arr

print(rotate([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]))
        
