valores=input()
logico1=valores.split()[0]
logico2=valores.split()[1]
print
if logico1 == "true" and logico2 == "true":
        retorno="true"
else:
        retorno="false"
print("%s" % (retorno))
