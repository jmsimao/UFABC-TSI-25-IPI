laco = True

while (laco):

    try:
        palavra = str(input())
     
        saida = ""
        for i in range(len(palavra)-1, -1, -1):
            saida += palavra[i] 
            
        print('%s' % (saida))

    except EOFError:
        laco = False