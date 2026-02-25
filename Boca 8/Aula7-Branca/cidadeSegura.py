
laco = True

def cidadeSegura(vetor, n):

    for linha in range(0, (n + 1)):
        saida = ""
        for col in range(0, n):
            superior = vetor[linha][col:col+2]
            inferior = vetor[linha+1][col:col+2]
            #print('lado superior: %s, lado inferior: %s' % (superior, inferior))

            qtdeCams = 0
            for c in range(0, 2):
                qtdeCams += 1 if (superior[c] == 1) else 0
                qtdeCams += 1 if (inferior[c] == 1) else 0
            #print('Total cam: %d' % qtdeCams)

            saida += 'S' if (qtdeCams >= 2) else 'U'

        print('%s' % saida)

while laco:
    try:
        n = int(input())

        vetor = [0] * (n + 1)
        for i in range(0, (n + 1)):
            entry = list(map(int, input().split()))
            vetor[i] = entry

        #print('n: %d, vetor: %s' % (n, vetor))

        cidadeSegura(vetor, n)

        #laco = False
    except:
        laco = False

#
