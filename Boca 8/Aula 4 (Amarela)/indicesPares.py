laco = True

def indicesPares(vetor):
    #print(vetor)

    ehVetorPar = ''; qtde = 0
    for i in range(0, len(vetor)):
        if (i % 2 == 0):
            ehVetorPar += str(vetor[i]) + ' '
            qtde += 1 if (vetor[i] % 2 == 0) else 0
        else:
            qtde += 1 if (vetor[i] % 2 == 0) else 0

    return [ehVetorPar, str(qtde)]

while (laco):
    try:
        qtde = int(input())
        vetorTemp = input().split()
        vetor = [0] * qtde
        for i in range(0, qtde):
            vetor[i] = int(vetorTemp[i])

        elementos, qtdeElementos = indicesPares(vetor)

        print('%s%s' % (elementos, qtdeElementos))
        laco = False

    except EOFError:
        laco = False
        break
