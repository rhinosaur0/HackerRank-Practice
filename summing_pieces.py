import sys


n = int(sys.stdin.readline().strip())

a = list(map(int, input().rstrip().split()))
a.insert(0, 0)

mod = 10 ** 9 + 7
all = [0] * (n + 1)
pre_all = [0] * (n + 1)
all[0] = pre_all[0] = 1

for i in range(1, n + 1):
    if i == 1:
        all[i] = 1
    else:
        all[i] = (all[i - 1] * 2) % mod
    pre_all[i] = (pre_all[i - 1] * 2) % mod

mul = 0
add = 0
dp = [0] * (n + 1)

for i in range(1, n + 1):
    mul = pre_all[i] - 1 % mod 
    # this is the number we are multiplying to the new number in the array
    # For every case, the number of times that the first element is added is equal to the last number added
        # First number is added for every case where the final element is part of the last subset, or not part of the last subset, hence 2 * mul
    # However, the last time that it is counted, the last element is in the same subset as the first element
    # This case is in a 1-1 correspondence to the case where element 1 was added i times. Thus we get 2 * mul + 1.

    dp[i] = (2 * dp[i - 1] + add + mul * a[i] % mod) % mod 
    # 2 * dp[i-1]
        # once for the case where the newly added element is in its own subset
        # once for the case where the newly added element is in the last subset
        # add accounts for the extra time where every element is in the last subset, where the position is i on the array
            # this occurs exactly 2 ** (i - 1) times, each time for each possible subset combination for the elements before

    add = (add + a[i] * pre_all[i - 1] % mod) % mod
    # must be added every time for a new iteration 

print(dp[n])
