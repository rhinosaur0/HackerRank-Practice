def getWays(n, coins):
    coins.sort()
    coinsCount = len(coins)
    ways = [[0 for b in range(coinsCount + 1)] for i in range(n + 1)]
    ways[0] = [1 for b in range(coinsCount + 1)]
    for i in range(n + 1):
        ways[i][0] = 1

    for k in range(coins[0], n + 1, coins[0]):
        ways[k][1] = 1
    for i in range(1, coinsCount): 
        for j in range(1, n + 1): 
            for k in range(j, -1, -coins[i]):
                ways[j][i + 1] = ways[j][i + 1] + ways[k][i]



    
    return ways[n][coinsCount]
