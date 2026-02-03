numeros = input()
base = int(numeros.split()[0])
expoente = int(numeros.split()[1])
print('%.4f' % (pow(base, expoente)))