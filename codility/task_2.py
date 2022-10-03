
def solution(X):
    lets = ["s", "m", "h", "d", "w"]
    past = 0
    i = 0
    next_rem = 1
    while next_rem and i < 4:
        if i < 2:
            if i:
                past = rem
            rem = X % 60
            X = X // 60
            next_rem = X // 60
            i += 1
        elif i == 2:
            if not past:
                past = rem
            rem = X % 24
            X = X // 24
            next_rem = X // 24
            i += 1
        elif i == 3:
            if not past:
                past = rem
            rem = X % 7
            X = X // 7
            next_rem = X // 7
            i += 1

    if past:
        rem += 1
    elif not X:
        return str(rem) + lets[i-1]
    date = str(X) + lets[i] + str(rem) + lets[i-1]
    return date

def solution2(X):
    weeks = X // (7 * 24 * 60 * 60)
    days = (X // (24 * 60 * 60)) - weeks * 7
    hours = (X // (60 * 60)) - days * 24
    minutes = (X // 60)  - hours * 60
    seconds = X - minutes * 60

    if weeks:
        p1 = weeks
        p11 = "w"
        if hours or minutes or seconds:
            days += 1
        p2 = days
        p22 = "d"
    elif days:
        p1 = days
        p11 = "d"
        if minutes or seconds:
            hours += 1
        p2 = hours
        p22 = "h"
    elif hours:
        p1 = hours
        p11 = "h"
        if seconds:
            minutes += 1
        p2 = minutes
        p22 = "m"
    elif minutes:
        p1 = minutes
        p11 = "m"
        p2 = seconds
        p22 = "s"
    else:
        return str(seconds) + "s"

    return str(p1) + p11 + str(p2) + p22

T = 1000000
print(solution2(T))
print(solution(T))
    