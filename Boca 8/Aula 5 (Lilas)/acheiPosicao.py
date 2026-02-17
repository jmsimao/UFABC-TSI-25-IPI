tam = int(input())
vetor = [0] * tam

literal = input().split()

for i in range(0, tam):
    vetor[i] = int(literal[i])

qtdeBusca = int(input())
vetResult = [0] * qtdeBusca

def busca(p, numero, vetor, vetResult):
    try:
        vetResult[p] = vetor.index(numero)

    except ValueError:
        vetResult[p] = -1

#print(vetor)

for i in range(0, qtdeBusca):
    busca(i, int(input()), vetor, vetResult)
    print(vetResult[i])
