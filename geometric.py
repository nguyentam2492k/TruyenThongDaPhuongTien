import math

def prob(n, p):
    return float( p * math.pow(1-p, n-1) )

def infoMeasure(n, p):
    return float( -math.log( prob(n, p), 2 ) )

def sumProb(N, p):
    '''
    sumProb: total of prob of all symbols from 1 to N
    VD: with p=0.75
        sumProb(10, 0.7) = 0.9999940950999998
        sumProb(20, 0.7) = 0.999999999965132
        sumProb(40, 0.7) = 0.9999999999999997

    so if N -> ∞ then sumProb(N, 0.7) -> 1
    '''
    sum = 0
    for i in range( 1, N+1 ):
        sum += prob(i, p)
    return float(sum)

def approxEntropy(N, p):
    '''
    approxEntropy function: avarage information sources of all symbols from 1 to N
    VD: with p = 0.5
        approxEntropy(10,0.5) = 1.98828125
        approxEntropy(50,0.5) = 1.9999999999999538
        approxEntropy(100,0.5) = 1.9999999999999998
            ...
    so if N -> ∞ then approxEntropy(N, 0.5) -> 2 ~ Entropy of geometric infomation source with p = 0.5
    '''
    sum = 0
    for i in range(1, N + 1):
        sum += ( prob(i, p) * infoMeasure(i, p) )
    return sum

print(approxEntropy(100, 0.5))