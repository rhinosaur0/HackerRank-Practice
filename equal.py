def equal(arr):
    arr.sort()
    value = [float('inf') for i in range(arr[-1] - arr[0] + 1)]
    def least(x):
        if x < 0:
            return float('inf')
        if x == 0:
            return 0
        if value[x] != float('inf'):
            return value[x]
        best = min(least(x - 1) + 1, least(x - 2) + 1, least(x - 5) + 1, value[x])
        value[x] = best
        return best
    
    a =[0 for i in range(5)]
    for c in range(5):
        for i in arr:
            b = least(arr[-1] - i + c)
            a[c] += b

    return min(a)
