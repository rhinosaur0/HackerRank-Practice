# work from the back

# case 1: last day prices are 1, skip
# case 2: last day prices > 1, go until the next biggest number 

# [1, 1, 1, 1, 9, 1, 10]

# 60 - 9 - 1 - 1 - 1 - 1 - 1 = 46

# 36 - 1 - 1 - 1 - 1 +

def stockmax(n, prices):
    answer = 0
    prices.reverse()
    current_max = prices[0]
    for i in range(n - 1):
        if prices[i + 1] >= prices[i]:
            current_max = prices[0]
        else:
            answer += current_max - prices[i + 1]

    return answer
        


