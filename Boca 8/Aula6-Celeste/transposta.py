n = int(input()); m = int(input())

vetOriginal = [0] * n


def transposta(vet, n, m):
    #vetOutput = [0] * m

    try:
        for k in range(m):
            linha = ""
            for u in range(n):
                linha += str(vet[u][k]) + ' '
            print(linha.rstrip())
    except:
        pass

try:
    for i in range(n):
        innerVet = list(map(int, input().split()))
        vetOriginal[i] = innerVet
except:
    pass

#print(vetOriginal)

transposta(vetOriginal, n, m)












