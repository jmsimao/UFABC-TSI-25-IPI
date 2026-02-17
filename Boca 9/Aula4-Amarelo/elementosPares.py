laco = True

def elementosPares(vetor):
    #print(vetor)

    ehPar = ''; qtde = 0
    for i in range(0, len(vetor)):
        if (vetor[i] % 2 == 0):
            ehPar += str(vetor[i]) + ' '; qtde += 1

    return [ehPar, str(qtde)]

while (laco):
    try:
        qtde = int(input())
        vetorTemp = input().split()
        vetor = [0] * qtde
        for i in range(0, qtde):
            vetor[i] = int(vetorTemp[i])

        elementos, qtdeElementos = elementosPares(vetor)

        print('%s%s' % (elementos, qtdeElementos))
        laco = False

    except EOFError:
        laco = False
        break
