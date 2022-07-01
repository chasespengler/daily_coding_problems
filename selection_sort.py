arr = [1, 5, 0, 7, 11, 26, 13, 12, 22]

def selection(arr):
    for i in range(len(arr)):
        minInd = i
        for x in range(i + 1, len(arr), 1):
            if arr[x] < arr[minInd]:
                minInd = x

        arr[i], arr[minInd] = arr[minInd], arr[i]

    return arr

print(selection(arr))