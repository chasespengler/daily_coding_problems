'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def perf(n):
    i = 19
    perfs = [i]
    while len(perfs) < n:
        i += 1
        if i > 1111111111:
            return "No more perfect numbers"
        sum = 0
        for val in str(i):
            sum += int(val)
        i = int(i)
        if sum == 10:
            perfs.append(i)

    return perfs[n-1]

print(perf(10000))