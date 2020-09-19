import math

def prob(n, p):
    return float( math.pow(p, n) )

def infoMeasure(n, p):
    return float( -math.log( prob(n, p), 2 ) )

def sumProb(N, p):
    '''
    :param N:
    :param p:
    :return:
    '''
    sum = 0
    for i in range( 1, N+1 ):
        sum += prob(i, p)
    return float(sum)

def aprroxEntropy(N, p):
    '''
    :param N:
    :param p:
    :return:
    '''
    sum = 0
    for i in range(1, N + 1):
        sum += ( prob(i, p) * infoMeasure(i, p) )
    return sum

