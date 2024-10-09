

def legoBlocks(m, n):

    MOD = 10 * 9 + 7

    if m == 1:
        return 1
    if n == 1 and m <= 4:
        return 1
    if n == 1:
        return 0
    if m == 2:
        return (2 ** n - 1) % MOD


    dprow = [0] * (m + 3)
    dprow[1] = 1
    dprow[2] = 2
    dprow[3] = 4
    dprow[4] = 8

    def perm_row(x):
        if x < 1:
            return 0
        if dprow[x] != 0:
            return dprow[x]
        dprow[x] = perm_row(x - 1) + perm_row(x - 2) + perm_row(x - 3) + perm_row(x - 4)
        return dprow[x]

    perm_row(m)
    print(dprow)

    valid_walls = [0] * (m + 1)
    invalid_walls = [0] * (m + 1)
    valid_walls[1] = 1
    invalid_walls[1] = 0
    valid_walls[2] = (2 ** n - 1) % MOD
    invalid_walls[2] = 1

    for i in range(3, m + 1):
        current_invalid = 0
        valid_walls[i] = dprow[i] ** n % MOD
        for j in range(1, i):
            current_invalid = current_invalid + valid_walls[i - j] * (invalid_walls[j] + valid_walls[i - j]) % MOD
        invalid_walls[i] = current_invalid % MOD
        valid_walls[i] = valid_walls[i] - invalid_walls[i] % MOD

    return valid_walls[m]


        
