import math

def giaithua(x):
    if x == 1:
        return 1
    else:
        return x * giaithua(x-1)

def prob( n, r, p):
    return float( ( giaithua(n) / ( giaithua(n-r+1)*giaithua(r-1) ) ) * math.pow(1-p, n-r) )

def infoMeasure(N, r, p):
    return float( - math.log( prob(N, r, p), 2 ) )

def sumProb(N, r, p):      #Tong xac xuat cua tat ca cac symbols tu 1 toi M
    sum = 0
    for i in range(1, N + 1):
        sum += prob(r, r, p)
    return float(sum)

def approxEntropy(N, r, p):
    sum = 0
    for i in range(1, N + 1):
        sum += (prob(i, r, p) * infoMeasure(i, r, p))
    return sum
