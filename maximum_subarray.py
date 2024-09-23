def maxSubarray(n, arr):
    dp = [float('-inf') for i in range(n + 1)]
    int2 = float('-inf')
    a = [float('-inf')]
    for i in range(n):
        dp[i + 1] = max(dp[i], arr[i], dp[i] + arr[i]) # subarray
        if arr[i] < 0:
            a.append(int2)
        int2 = max(arr[i], int2 + arr[i]) # subsequence
            


    return max(max(a), int2), dp[n]
