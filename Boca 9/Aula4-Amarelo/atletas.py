quantidade = 100
idade = [0] * quantidade
altura = [0.0] * quantidade
peso = [0.0] * quantidade
genero = [''] * quantidade

hmQuantidade = 0
fmQuantidade = 0
hmAlturaTotal = 0.0
fmPesoTotal = 0.0

for i in range(0, quantidade):
    idade[i] = int(input())
    altura[i] = float(input())
    peso[i] = float(input())
    genero[i] = str(input())

    if (genero[i] == 'M'):
        hmAlturaTotal += altura[i]
        hmQuantidade += 1
    else:
        fmPesoTotal += peso[i]
        fmQuantidade += 1


# Média da altura e peso.
hmMediaAltura = 0.0; fmMediaPeso = 0.0

if (hmQuantidade > 0):
    hmMediaAltura = hmAlturaTotal / hmQuantidade

if (fmQuantidade > 0):
    fmMediaPeso = fmPesoTotal / fmQuantidade

## Quantidade acima da altura (masc) e abaixo do peso (fem).
hmQtdAcimaAltura = 0; fmQtdAbaixoPeso = 0

for i in range(0, quantidade):
    if (hmQuantidade > 0 and genero[i] == 'M' and altura[i] > hmMediaAltura):
        hmQtdAcimaAltura += 1
    elif (fmQuantidade > 0 and genero[i] == 'F' and peso[i] < fmMediaPeso):
        fmQtdAbaixoPeso += 1

if (hmQtdAcimaAltura > 0):
    hmMensagem = 'Ha ' + str(hmQtdAcimaAltura) + ' atletas homens acima da media da altura dos homens.'
else:
    hmMensagem = 'Nao houve entrada de atletas homens.'

if (fmQtdAbaixoPeso > 0):
    fmMensagem = 'Ha ' + str(fmQtdAbaixoPeso) + ' atletas mulheres abaixo da media do peso das mulheres.'
else:
    fmMensagem = 'Nao houve entrada de atletas mulheres.'

print(hmMensagem)
print(fmMensagem)
