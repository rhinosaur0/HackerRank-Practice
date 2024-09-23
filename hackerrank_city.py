import sys
sys.set_int_max_str_digits(10000000000)
def hackerrankCity(A):
    n, sTotal, sCorner, maxCorner = 1, 0, 0, 0
    for i in range(len(A)):
        
        n, sTotal,sCorner,maxCorner = 4*n + 2, 4*sTotal + (12*n+8)*sCorner + A[i]*(1 + 16*n**2 + 12*n), 4*sCorner + A[i]*(8*n+3) + maxCorner*(3*n+2), maxCorner*2+3*A[i]
    return sTotal % (10 ** 9 + 7)
