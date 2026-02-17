
def numerosParesEImparesAB(de, ate):
    pares = ''; impares = ''
    for i in range(de, ate+1):
        pares += (str(i) + ' ') if ((i % 2 )== 0) else ''
        impares += (str(i) + ' ') if ((i % 2 != 0)) else ''
    return [pares.rstrip(), impares.rstrip()]

de, ate = input().split()
pares, impares = map(str, numerosParesEImparesAB(int(de), int(ate)))

print('%s' % pares)
print('%s' % impares)
