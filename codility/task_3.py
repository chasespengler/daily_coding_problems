
def solution(S, B):
    R = [None] * len(B)
    B = list(map(float, B))
    C = B.copy()
    total = sum(B)
    rem = 0
    for i in range(len(B)-1, -1, -1):
        my_val = float(S) * B[i] / total
        if not i:
            my_val += rem
        val = "{:.2f}".format(my_val)
        if float(val) - my_val:
            rem += my_val - float(val)

        R[C.index(B[i])] = val

    return R

print(solution("1.00", ["1.00", "0.05"]))
