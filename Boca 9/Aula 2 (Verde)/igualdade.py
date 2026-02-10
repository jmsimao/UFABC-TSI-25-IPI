numeros=input()
numA=int(numeros.split()[0])
numB=int(numeros.split()[1])
if numA==numB:
    retorno="true"
else:
    retorno="false"
print("%s" %(retorno))

