operacao = str(input())
dimensao = int(input())

vLine = [0] * dimensao

for i in range(0, len(vLine)):
    # Literal da Linha
    litLinha = input().split()
    #print(litLinha)

    vLine[i] = vCol = [0] * dimensao
    for j in range(0, len(litLinha)):
        vLine[i][j] = int(litLinha[j])

#print(vLine)
#print(vLine[2][2])

def soma(vLine):
    ret = 0
    for i in range(0, len(vLine)):
        ret += vLine[i][i]
    return ret

def media(vLine):
    ret = 0
    for i in range(0, len(vLine)):
        ret += vLine[i][i]
    return (ret / len(vLine))

result = 0.0

if (operacao.upper() == 'S'):
    result = soma(vLine)
else:
    result = media(vLine)

print('%.1f' % result)
