dimensao = int(input())
vetor = [0] * dimensao


def somaMat2(vetor):
    soma = 0
    for l in range(1, len(vetor)):
        for c in range(0, (l)):
            #print(vetor[l][c])
            soma += vetor[l][c]
    print('%d' % soma)

for i in range(0, dimensao):
    try:
        colEntry = input().split()
        vetorLinha = [0] * dimensao
        for l in range(0, dimensao):
            vetorLinha[l] = int(colEntry[l])
        vetor[i] = vetorLinha

    except EOFError:
        pass

somaMat2(vetor)
