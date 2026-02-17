laco = True

while (laco):

    try:
        palavra = str(input())

        saida = ""
        for i in range(0, len(palavra)):
            saida += str(palavra[i])
            if (i < len(palavra)-1):
                saida += ' '

        #print(len(saida))
        print('%s' % (saida))

    except:
        laco = False
