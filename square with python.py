def s (n):
    ss= 0
    for i in range (1, n+1):
        ss += i
    return ss**2


def sa (n):
    ss = 0
    for i in range(1, n+1):
        ss += (i**2)
    return ss


def minus (n, m):
    return n - m

a = s(10)
b = sa(10)
print(minus(a, b))