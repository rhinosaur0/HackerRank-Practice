def candies(n, arr):
    candies = [1 for i in range(n)]
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, 0, -1):
        if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    return sum(candies)
