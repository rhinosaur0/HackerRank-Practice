def kMarsh(m, n, grid):
    answer = 0
    verticalX = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            verticalX[i][j] = i if grid[i - 1][j - 1] == 'x' else verticalX[i-1][j]
            
    for i in range(2, m + 1):
        horizX = [-2] * i
        for j in range(2, n + 1):
            if grid[i - 1][j - 2] == 'x':
                continue
            if grid[i - 1][j - 1] == 'x':
                horizX = [-2] * i
                continue
            for k in range(1, i):
                if grid[k - 1][j - 1] == 'x' or grid[k - 1][j - 2] == 'x':
                    horizX[k] = -2
                    continue
                if horizX[k] == -2 and verticalX[i][j - 1] < k:
                    horizX[k] = j - 1
                if horizX[k] > 0 and verticalX[i][j] < k:
                    answer = max(answer, 2 * (i - k + j - horizX[k]))
                    
    return 'impossible' if answer == 0 else answer
