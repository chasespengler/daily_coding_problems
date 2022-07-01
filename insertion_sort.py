arr = [1, 5, 0, 7, 11, 26, 13, 12, 22, 3]

def insertion(arr):
    for i in range(1, len(arr), 1):
        key = arr[i]
        for x in range(i - 1, -1, -1):
            if key >= arr[x]:
                break
            elif arr[x] > key:
                arr[x + 1], arr[x] = arr[x], arr[x + 1]
            else:
                arr[x - 1] = key

    return arr

print(insertion(arr))