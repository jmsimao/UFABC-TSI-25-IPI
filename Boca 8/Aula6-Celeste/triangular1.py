n = int(input())

vetor = [0] * n

def triangular1(vetor, n):
    ret = 'SIM'
    for l in range(0, n):
        for c in range(0, l):
            if (ret == 'SIM' and vetor[l][c] > 0):
                ret = 'NAO'
            #print(vetor[l][c])

    return ret

try:
    for i in range(n):
        innerVetor = list(map(int, input().split()))
        vetor[i] = innerVetor
except:
    pass

#print(vetor)
print('%s' % triangular1(vetor, n))
