lin, col = input().split()
lin = int(lin); col = int(col)

vetor = [0] * lin

def somaMat5(vetor, lin, col):
    somaTotal = 0
    for i in range(0, len(vetor)):
        for j in range(0, col):
            somaTotal += vetor[i][j]
    print('Somatorio da Matriz: %d' % somaTotal)


for i in range(0, lin):
    colEntry = input().split()

    vetCol = [0] * col
    for j in range(0, col):
        vetCol[j] = int(colEntry[j])
    vetor[i] = vetCol

#print(vetor)
somaMat5(vetor, lin, col)
