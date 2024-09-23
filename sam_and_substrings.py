def substrings(n):
    answerT = 0
    answer2 = 0
    a = [int(d) for d in str(n)] # converting integar into its digits
    for b in range(len(a)):
        answer2 = answer2 * 10 + a[b] * (b+1)
        answerT = answerT + answer2
    return answerT
