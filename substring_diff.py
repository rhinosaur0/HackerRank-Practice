def substringDiff(k, s1, s2):
    answer = 0
    dp=[]
    for i in range(1, len(s1) + len(s2)):
        dp.append([])
        for j in range(i):
            if len(s1) - j >= 1 and i - j < len(s2) + 1:
                if s1[len(s1) - j - 1] == s2[i - j - 1]: # creates a list of diagonals in the s1 s2 array
                    dp[-1].append(1)
                else:
                    dp[-1].append(0) 

    for i in dp:
        left = 0
        zeroCount = 0
        for right in range(len(i)):

            if i[right] == 0:
                zeroCount += 1
        
            while zeroCount > k:
                if i[left] == 0:
                    zeroCount -= 1
                left += 1
        
            answer = max(answer, right - left + 1)

    return answer
