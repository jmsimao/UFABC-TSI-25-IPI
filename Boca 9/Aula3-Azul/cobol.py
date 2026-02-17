
def graceHooper(expressao):
    parcela = str(expressao).lower(); palavra = 'cobol'; letrasIniciais = ''; letrasFinais = ''

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

    print('Letras iniciais: %s, Letras finais: %s' % (letrasIniciais, letrasFinais))

    juntar = letrasIniciais + letrasFinais
    
    qtde = 0; 

    juncao = ''; c = 0
    for i in range(len(letrasFinais)):
        juncao += letrasIniciais[i+c:i+c+1] + letrasFinais[i+c:i+c+1]
        c += 1


    print(juncao)



    print('Total de letras: %d.' % qtde)    

    if (letrasIniciais == 'cobol' or letrasFinais == 'cobol' or qtde == 5):
        return 'GRACE HOPPER'
    else:
        return 'BUG'


laco = True

while (laco):

    try:
        print('%s' % (graceHooper(str(input()))))
        print('---')

    except EOFError:
        #print('end')
        laco = False
