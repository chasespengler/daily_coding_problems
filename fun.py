import yfinance as yf
from statistics import mean, stdev

nums = [1, 4, 7, 8, 9, -14]

'''
for i in range(1000):
    for num in nums:
        eq = nums.pop(num)
'''

z = 1041
#print(format(z, "b"))

def solution(N):
    # write your code in Python 3.6
    b = format(N, "b")

    max_gap = 0
    cur_gap = 0
    for i in range(len(str(b))-1):
        dig1 = b[i]
        dig2 = b[i+1]
        print(b)
        print(dig1, dig2)
        print(cur_gap)
        print(max_gap)
        if dig1 == "1" and dig2 == "0":
            cur_gap += 1
        elif dig1 == "0" and dig2 == "1":
            if cur_gap > max_gap:
                max_gap = cur_gap
            cur_gap = 0
        elif dig1 == "0" and dig2 == "0":
            cur_gap += 1

    return max_gap

y = yf.download('RITM').Close.pct_change().dropna().values
print(y)
print(mean(y))
print(stdev(y))