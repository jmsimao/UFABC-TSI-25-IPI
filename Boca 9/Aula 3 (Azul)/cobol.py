
def graceHooper(expressao):
    parcela = str(expressao).lower(); letrasIniciais = ''; letrasFinais = ''

    for i in range(0, expressao.count('-')):
        #print(parcela.index('-'))
        letrasIniciais += parcela[0]
        letrasFinais += parcela[parcela.index('-')-1:parcela.index('-')]
        parcela = parcela[parcela.index('-')+1:]
        #print(parcela)
       
    if (not parcela == ''):
         letrasIniciais += parcela[0]
         letrasFinais += parcela[len(parcela)-1]
         #print(len(parcela))
        
         #letrasFinais += parcela[len(parcela):]

    #print(letrasIniciais, letrasFinais)

    #print(letras)
    if (letrasIniciais == 'cobol' or letrasFinais == 'cobol'):
        return 'GRACE HOOPER'
    else:
        return 'BUG'


laco = True

while (laco):

    try:
        print('%s' % (graceHooper(str(input()))))

    except EOFError:
        #print('end')
        laco = False
