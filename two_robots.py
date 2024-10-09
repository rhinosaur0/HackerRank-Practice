def twoRobots(m, queries):
    
    dp = [(0, 0, 0)] * m  # total distance, first robot position, second robot position
    dp[0] = (abs(queries[0][1] - queries[0][0]), 0, 0)

    for i in range(1, m):
        a, b = queries[i]
        x, y = dp[i-1][1], dp[i-1][2]
        if abs(x - a) > abs(x - b):
            pass


def twoRobots(m, queries):


    # from above the array, robot 1 is going to take the next mission
    # from left of the array, robot 2 is going to take the next mission

    dp = [[(0, 0, 0) for i in range(m + 1)] for j in range(m + 1)] # total distance, first robot position, second robot position
    dp[1][0] = (abs(queries[0][1] - queries[0][0]), queries[0][1], 0)
    dp[0][1] = (abs(queries[0][1] - queries[0][0]), 0, queries[0][1])

    for i in range(1, m):
        dp[0][i + 1] = (dp[0][i][0] + abs(queries[i][1] - queries[i][0]) + abs(queries[i][0] - dp[0][i][2]), 0, queries[i][1])
        dp[i + 1][0] = (dp[i][0][0] + abs(queries[i][1] - queries[i][0]) + abs(queries[i][0] - dp[i][0][1]), queries[i][1], 0)

    for i in range(1, m):
        for j in range(1, m + 1 - i):
            distance_to_travel = abs(queries[i + j - 1][0] - queries[i + j - 1][1])
            first_robot_distance = dp[i - 1][j][0] + abs(dp[i - 1][j][1] - queries[i + j - 1][0]) + distance_to_travel
            second_robot_distance = dp[i - 1][j][0] + abs(dp[i][j][2] - queries[i + j - 1][0]) + distance_to_travel

            if first_robot_distance < second_robot_distance:
                dp[i][j] = (first_robot_distance, queries[i + j - 1][1], dp[i - 1][j][2])
            else:
                dp[i][j] = (second_robot_distance, dp[i][j - 1][1], queries[i + j - 1][1])

    possible = []
    for i in range(m):
        if dp[i][m - i][0] != 0:
            possible.append(dp[i][m - i][0])
    for i in dp:
        print(f"\n{i}")
    return min(possible)

print(twoRobots(4, [(1, 5), (3, 2), (4, 1), (2, 4)]))


# does not matter which robot it is, only care about where the robot ends up
def twoRobots(m, n, queries):
    dp = [[float('inf')] * (m + 1) for _ in range(n)]
    endstate = {0}
    dp[0][0] = abs(queries[0][1] - queries[0][0])

    for i in range(1, n):
        for j in endstate:
            # this considers the case where the second robot stays exactly where it is and the first robot goes from the previous 
            # position of the last task to finish the new task
            dp[i][j] = dp[i - 1][j] + abs(queries[i][0] - queries[i - 1][1]) + abs(queries[i][1] - queries[i][0])

        temp = float('inf')

        for k in endstate:
            # this considers the case where the second robot completes the task
            if k == 0:
                temp = min(temp, dp[i - 1][0] + abs(queries[i - 1][0] - queries[i - 1][1]))
            else:
                temp = min(temp, dp[i - 1][k] + abs(queries[i - 1][0] - k) + abs(queries[i - 1][1] - queries[i - 1][0]))
        
        dp[i][queries[i - 1][1]] = min(temp, dp[i][queries[i-1][1]])
        endstate.add(queries[i - 1][1])

    return min(dp[n - 1])






