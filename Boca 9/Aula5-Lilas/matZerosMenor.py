lin, col = input().split()
lin = int(lin); col = int(col)

vetor = [0] * lin

def matZeroMenor(vetor, lin, col):
    zeros = 0; indice = 0; menor = 0
    for i in range(0, lin):
        for j in range(0, col):
            zeros += 1 if (j == col-1 and vetor[i][col-1] == 0) else 0
            if (i == 0 and j == 0):
                indice = 1; menor = vetor[i][j]
            else:
                if (vetor[i][j] < menor):
                    indice = i+1; menor = vetor[i][j]

    print('%d zero(s)' % zeros)
    print('%d linha %d' % (menor, indice))


for i in range(0, lin):
    colEntry = input().split()

    vetCol = [0] * col
    for j in range(0, col):
        vetCol[j] = int(colEntry[j])
    vetor[i] = vetCol

#print(vetor)
matZeroMenor(vetor, lin, col)
