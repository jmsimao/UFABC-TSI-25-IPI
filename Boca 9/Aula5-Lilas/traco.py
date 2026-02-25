num = int(input())

vetor = [0] * num

def traco(vetor, n):
    soma = 0
    for l in range(n):
        for c in range(l, l+1):
            soma += vetor[l][c]
    return soma

try:
    for i in range(num):
        innerVetor = list(map(int, input().split()))
        vetor[i] = innerVetor

except:
    print('Erro')
    pass

#print(vetor)
print('%d' % traco(vetor, num))
