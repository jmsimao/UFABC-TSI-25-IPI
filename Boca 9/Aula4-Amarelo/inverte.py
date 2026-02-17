laco = True

def inverte(vetor):

    retorno = ''
    vetorInverso = vetor[::-1]
    for i in range(0, len(vetorInverso)):
        retorno += str(vetorInverso[i]) + ' '
   
    return retorno.rstrip()

while (laco):
    try:
        qtde = int(input()); vetorTemp = input().split()
        vetor = [0] * qtde; vetorOrdem = ''
        for i in range(0, qtde):
            vetorOrdem += vetorTemp[i] + ' '
            vetor[i] = int(vetorTemp[i])

        print('%s' % (vetorOrdem.rstrip()))
        print('%s' % (inverte(vetor)))
        laco = False

    except EOFError:
        laco = False
        break
