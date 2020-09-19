import math

def giaithua(x):
    if x == 1:
        return 1
    else:
        return x * giaithua(x-1)

def prob(N, r, n, p):
    return float( ( giaithua(N) / ( giaithua(n)*giaithua(N-n) ) ) * math.pow(p, N) )

def infoMeasure(N, r, n, p):
    return float( - math.log( prob(N, n, p), 2 ) )

def sumProb(N, r, M, p):      #Tong xac xuat cua tat ca cac symbols tu 1 toi M
    sum = 0
    for i in range(1, M + 1):
        sum += prob(N, i, p)
    return float(sum)

def aprroxEntropy(N, r, M, p):
    sum = 0
    for i in range(1, M + 1):
        sum += (prob(N, i, p) * infoMeasure(N, i, p))
    return sum
