laco = True

def menorPosicao(vetor):
    #print(vetor)

    menorValor = 0; posicao = 0
    for i in range(0, len(vetor)):
        if (i == 0):
            posicao = i
            menorValor = vetor[i]
        else:
            if (vetor[i] <= menorValor):
                posicao = i
                menorValor = vetor[i]

    return [str(menorValor), str(posicao)]

while (laco):
    try:
        qtde = int(input())
        vetorTemp = input().split()
        vetor = [0] * qtde
        for i in range(0, qtde):
            vetor[i] = int(vetorTemp[i])

        menorValor, posicao = menorPosicao(vetor)

        print('Menor valor: %s' % (menorValor))
        print('Posicao: %s' % (posicao))
        laco = False

    except EOFError:
        laco = False
        break
