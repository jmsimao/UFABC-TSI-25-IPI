
def numerosParesAB(de, ate):
    pares = ''
    for i in range(de, ate+1):
        pares += (str(i) + ' ') if ((i % 2 )== 0) else ''

    return pares.rstrip()

de, ate = input().split()
literal = numerosParesAB(int(de), int(ate))
print('%s' % literal)
