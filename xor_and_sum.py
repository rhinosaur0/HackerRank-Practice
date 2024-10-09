# ^ is the xor operator 

def xorAndSum(a, b):
    sum = 0
    N = 314159
    a = str(a)
    alist = [0]
    for i in a[::-1]:
        alist.append(alist[-1] + int(i))
    alist = alist + [alist[-1]] * (5000000 - len(a))

    print(alist[:10])

    b = str(b)
    blist = [0]
    for i in b[::-1]:
        blist.append(blist[-1] + int(i))
    blist = blist + [blist[-1]] * (5000000 - len(b))

    print(blist[:10])
    
    powers = [1]

    for i in range(414160):
        powers.append(powers[-1] * 2 % (10 ** 9 + 7))

    for i in range(414160):
        fac = powers[i]
        if alist[i + 1] == alist[i]: # calculate the sums from the b bits
            # sum += blist[max(0, i - N) : i + 1].count(1) * fac
            sum += (blist[i + 1] - blist[max(0, i - N)]) * fac
            
        else: # calculate the sums from the a bits
            # sum += (N + 1 - blist[max(0, i - N) : i + 1].count(1)) * fac
            sum += (N + 1 - blist[i + 1] + blist[max(0, i - N)]) * fac
            



    return sum % (10 ** 9 + 7)




print(xorAndSum(10, 1010))
