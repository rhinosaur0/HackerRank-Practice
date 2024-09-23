def countArray(n, k, x):
    d, s = 1, 0
    for i in range(2, n):
        d, s = s + d * (k - 2), d * (k - 1)
    return s if x == 1 else d
