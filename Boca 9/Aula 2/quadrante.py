valores = input().split()
posX = float(valores[0]); posY = float(valores[1])

if (posX == 0 and posY == 0):
    ret = 'Origem'

if (posX == 0 and posY < 0):
    ret = 'Eixo Y'
elif (posX > 0 and posY == 0):
    ret = 'Eixo X'

if (posX > 0 and posY > 0):
    ret = 'Q1'
elif (posX > 0 and posY < 0):
    ret = 'Q4'

if (posX < 0 and posY > 0):
    ret = 'Q2'
elif (posX < 0 and posY < 0):
    ret = 'Q3'

print('%s' % ret)