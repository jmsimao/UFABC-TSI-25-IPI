qtdeVet1 = int(input())
qtdeVet2 = int(input())

def classifica(vet, q1, q2):
    vetO = [0] * (q1 + q2)

    for i in range(0, len(vet)):
        #print('Posição %d, vetor %s' % (i, vetO))

        if (i == 0):
            vetO[i] = vet[i]
        else:
            vetO[i] = vet[i]
            #print('Atribuido a posição %d ao vetor: %s' % (i, vetO))
            for j in range(i, 0, -1):
                #print('Regresso de j: %d' % j)
                if (vetO[j] < vetO[j-1]):
                    menor = vetO[j]; maior = vetO[j-1]
                    #print('Valor menor: %d, valor maior %d.' % (menor, maior))
                    vetO[j-1] = menor; vetO[j] = maior

    #print('Ordernado: %s' % vetO)
    return vetO

vet1 = [0] * qtdeVet1
vet2 = [0] * qtdeVet2
vet3 = [0] * (qtdeVet1 + qtdeVet2)

for i in range(0, qtdeVet1):
    vet1[i] = int(input())
    vet3[i] = vet1[i]

for i in range(0, qtdeVet2):
    vet2[i] = int(input())
    vet3[i+qtdeVet1] = vet2[i]

vetorOrdenado = classifica(vet3, qtdeVet1, qtdeVet2)
#print('Vetor NAO ordenado: %s' % vet3)
#print('Vetor ordenado: %s' % vetorOrdenado)
for i in range(len(vetorOrdenado)):
    print('%d' % vetorOrdenado[i])
