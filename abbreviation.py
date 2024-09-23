def abbreviation(a, b):
    dp = [[1] + [0] * len(b) for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            elif a[i - 1] == b[j-1].lower():
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
            elif a[i-1].isupper():
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j]

    return 'YES' if dp[len(a)][len(b)] else "NO"
