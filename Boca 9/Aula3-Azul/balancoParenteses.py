
def balancoParenteses(expressao):
    retorno = 'correct'
    totalParenteses = expressao.count('(') + expressao.count(')')
    #print(expressao)
    
    if (totalParenteses % 2 != 0):
        retorno = 'incorrect'
    else:
        parentesesFecha = expressao.find(')'); parentesesAbre = expressao.find('(')
        #print(abre, fecha)

        if (parentesesFecha < parentesesAbre):
            retorno = 'incorrect'
        else:
            p1 = 0; p2 = 0; p3 = 0
            for i in range(len(expressao)):
                if (expressao[i] in '()'):
                    p1 += 1 if expressao[i] == '(' else 0
                    p2 += 1 if expressao[i] == ')' else 0
                    p3 = (p1 - p2)
                    #print(p3)

                    if (p3 < 0):
                        retorno = 'incorrect'
                        break
     
                    #print('P1 %d + P2 %d = P3: %d' % (p1, p2, p3))
    return retorno

try:
   #while (True):
    expressao = str(input())
    print('%s' % balancoParenteses(expressao))
 
except EOFError:
    pass