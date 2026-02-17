laco = True

def maiorElemento(vetor):

    maiorElemento = 0; posicao = 0

    for i in range(0, len(vetor)):
        if (i == 0):
            posicao = i; maiorElemento = vetor[i]
        elif (i > 0 and vetor[i] > maiorElemento):
            posicao = i; maiorElemento = vetor[i]

    return [posicao, maiorElemento]


while (laco):
    try:
        tamVetor = int(input())
        if (tamVetor == 0):
            laco = False
        else:
            vetorTemp = input().split()

            vetor = [0] * tamVetor
            for i in range(0, tamVetor):
                vetor[i] = int(vetorTemp[i])

            posicao, maiorElem = maiorElemento(vetor)

            print('%d %d' % (posicao, maiorElem))

    except EOFError:
        laco = False
        break

