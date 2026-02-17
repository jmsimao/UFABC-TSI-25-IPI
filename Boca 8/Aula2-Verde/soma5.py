enquanto = True
soma = 0

while (enquanto):
    numero = int(input())

    if (numero != 0):
        soma += numero
    else:
        enquanto = False
        print('%d' % (soma))