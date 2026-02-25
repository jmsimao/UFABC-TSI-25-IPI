
n = int(input())

matriz = [0] * n

def triangular2(matriz, n):
    triang2 = [True, True]

    for l in range(1, n):
        #print(list(map(str, matriz[l][0:l])))
        for c in range(0, l):
            #print('superior, Linha: %d, Col: %d = %d' % (l, c, matriz[l][c]))
            if (triang2[0] == True and matriz[l][c] > 0):
                triang2[0] = False

    for l in range(0, n):
        #print(list(map(str, matriz[l][l+1:n])))
        for c in range(l+1, n):
            #print('superior, Linha: %d, Col: %d = %d' % (l, c, matriz[l][c]))
            if (triang2[1] == True and matriz[l][c] > 0):
                triang2[1] = False

    if (triang2[0] == False and triang2[1] == False):
        ret = 'NAO'
    elif (triang2[0] == True and triang2[1] == True):
        ret = 'SIM: DIAGONAL'
    elif (triang2[0] == True and triang2[1] == False):
        ret = 'SIM: SUPERIOR'
    else:
        ret = 'SIM: INFERIOR'
    return ret

for i in range(n):
    innerVetor = list(map(int, input().split()))
    matriz[i] = innerVetor

#print(matriz)

print('%s' % triangular2(matriz, n))
