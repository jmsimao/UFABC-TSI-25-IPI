valores=input()
numA=valores.split()[0]
numB=valores.split()[1]
retorno=""
if (numA == "true" or numA == "false") or (numA == "true" or numA == "false"):
    if numA == "true":
        numA = True
    else:
        numA = False
    if numB == "true":
        numB = True
    else:
        numB = False
    retorno=(numA ^ numB)
    retorno=str(retorno).lower()
print("%s" % (retorno))