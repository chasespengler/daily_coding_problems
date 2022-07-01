arr = [1, 5, 0, 7, 11, 26, 13, 12, 22]

def bubble(arr):
    for i in range(len(arr)):
        for x in range(len(arr) - i - 1):
            if arr[x + 1] < arr[x]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]

    return arr

print(bubble(arr))
