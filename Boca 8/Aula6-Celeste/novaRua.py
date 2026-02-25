ns, lo = input().split()
ns = int(ns); lo = int(lo)

vetor = [0] * ns

def novaAvenida(vetor, ns, lo):
    menorValor = 0

    for l in range(0, ns):
        soma = 0
        for c in range(0, lo):
            soma += vetor[l][c]

        if (l == 0):
            menorValor = soma
        else:
            if (soma < menorValor):
                menorValor = soma
        #print(soma)

    print(menorValor)

try:
    for l in range(0, ns):
        innerVetor = [0] * lo
        entry = input().split()

        for c in range(0, lo):
            innerVetor[c] = int(entry[c])
        vetor[l] = innerVetor
except:
    pass

#print(vetor)

novaAvenida(vetor, ns, lo)
