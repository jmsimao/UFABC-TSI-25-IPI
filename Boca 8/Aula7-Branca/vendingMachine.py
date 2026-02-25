laco = True

def troco(valores, moedas):
    m = valores[0]  # valor do troco
    INF = m + 1     # infinito "grande o suficiente"

    # dp[i] = menor nº de moedas para fazer troco i
    dp = [INF] * (m + 1)
    dp[0] = 0       # 0 moedas para fazer troco 0

    for valor in moedas:
        for troco_atual in range(valor, m + 1):
            dp[troco_atual] = min(dp[troco_atual], dp[troco_atual - valor] + 1)

    if dp[m] >= INF:
        return 'impossivel'
    else:
        return dp[m]

def classifica(vetor):
    qtde = len(vetor);
    for i in range(qtde):

        for j in range(i, 0, -1):
            atual = vetor[j]; ant = vetor[j-1]
            if (atual < ant):
                vetor[j-1] = atual; vetor[j] = ant
            else:
                vetor[j] = atual; vetor[j-1] = ant
            #print('Classificando... ', vetor)

    #print('Class.Final: ', vetor)
    return vetor

while laco:
    try:
        valores = list(map(int, input().split()))
        m = valores[0]
        #print(m)
        if (m == 0):
            #print("\n")
            break
        else:
            moedas = list(map(int, input().split()))
            #print(valores)
            #print('moedas', moedas)
            moedas = classifica(moedas)

            ret = troco(valores, moedas)
            print(ret)

    except:
        laco = False


