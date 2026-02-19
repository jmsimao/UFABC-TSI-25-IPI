lin = int(input())
linMatriz = lin * 2
vetor = [0] * linMatriz

def somaMat(vetor, col):
    somaTotal = 0; sep = int(len(vetor) / 2)
    for i in range(0, sep):
        linha = ''
        for c in range(0, col):
            linha += str(vetor[i][c] + vetor[i+sep][c]) +  ' '
        print(linha.rstrip())

for i in range(0, linMatriz):
    try:
        colEntry = input().split()

        vetCol = [0] * lin
        for j in range(0, lin):
            vetCol[j] = int(colEntry[j])
        vetor[i] = vetCol

    except:
       pass

#print(vetor)
somaMat(vetor, lin)
