lin, col = input().split()
lin = int(lin); col = int(col)

vetor = [0] * lin

def somaMat6(vetor, lin, col):
    somaTotal = 0
    for i in range(0, len(vetor)):
        somaLinha = 0
        for j in range(0, col):
            somaLinha += vetor[i][j]
        print('Somatorio da Linha %d: %d' % (i, somaLinha))
        somaTotal += somaLinha
    print('Somatorio Matriz: %d' % somaTotal)


for i in range(0, lin):
    colEntry = input().split()

    vetCol = [0] * col
    for j in range(0, col):
        vetCol[j] = int(colEntry[j])
    vetor[i] = vetCol

#print(vetor)
somaMat6(vetor, lin, col)
