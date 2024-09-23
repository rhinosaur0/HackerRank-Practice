def cost(n, B):
    values = [0 for i in range(n + 1)]
    ready = [False for i in range(n + 1)]
    values[0] = 0
    values[1] = B[1] - 1
    ready[0] = True
    ready[1] = True
    def maximum(x):
        if x < 0:
            return -9999999
        if ready[x]:
            return values[x]
        
        a = maximum(x - 2) + B[x - 2]
        b = maximum(x - 3) + B[x - 3]

        if a >= b:
            values[x] = a + B[x] - 2
        else:
            values[x] = b + B[x] - 2
        ready[x] = True
        return values[x]
    
    return max(maximum(n - 1), maximum(n - 2) + B[-2] - 1)
