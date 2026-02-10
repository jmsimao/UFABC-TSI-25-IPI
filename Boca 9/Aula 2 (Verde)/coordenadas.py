valores = input().split()

valorX = float(valores[0])
valorY = float(valores[1])

ret = ""

if (valorX == 0.0 and valorY == 0.0):
    ret = "Origem"

if (valorX == 0.0 and valorY != 0.0):
    ret = "Eixo Y"

if (valorY == 0.0 and valorX != 0.0):
    ret = "Eixo X"

if (valorX > 0.0 and valorY > 0.0):
    ret = 'Q1'


if (valorX < 0.0 and valorY > 0.0):
    ret = 'Q2'

if (valorX < 0.0 and valorY < 0.0):
    ret = 'Q3'
    
if (valorX > 0.0 and valorY < 0.0):
    ret = 'Q4'

print(ret)