from math import pow
valores=input()
base=int(valores.split()[0])
expoente=int(valores.split()[1])
resultado=pow(base, expoente)
print('%.4f' % (resultado))