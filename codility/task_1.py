z = [10, 6, 6, 8]

def solution(X, B, Z):
    if len(B) == 0:
        return -1
    elif len(B) < Z:
        Z = len(B)
    avg_rate = sum(B[-Z:]) / Z

    size_left = X - sum(B)
    est = size_left / avg_rate
    if est % 1:
        est = int(est) + 1
    else:
        est = int(est)

    return est

print(solution(100, z, 2))