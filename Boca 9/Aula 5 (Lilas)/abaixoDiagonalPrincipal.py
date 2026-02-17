operacao = str(input())
dimensao = int(input())

vLine = [0] * dimensao

for i in range(0, len(vLine)):
    litLinha = input().split()

    vCol = [0] * dimensao

    for j in range(0, len(litLinha)):
        vCol[j] = int(litLinha[j])
    #print(vCol)
    vLine[i] = vCol

#print(vLine)
#print(vLine[2][3])

def soma(vLine):
    ret = 0
    for i in range(0, len(vLine)):
        for j in range(0, i):
            ret += 0 if (i == 0) else vLine[i][j]
    return ret

def media(vLine):
    ret = 0; qtde = 0
    for i in range(0, len(vLine)):
        for j in range(0, i):
            ret += 0 if (i == 0) else vLine[i][j]
            qtde += 0 if (i == 0) else 1
    return (ret / qtde)

result = 0.0

if (operacao.upper() == 'S'):
    result = soma(vLine)
else:
    result = media(vLine)

print('%.1f' % result)
