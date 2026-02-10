laco = True; maior = ""

while (laco):
    try:
        entrada = str(input())

        if (len(entrada) > len(maior)):
            maior = entrada
  
    except EOFError:
        laco = False
        if (maior == ""):
            print('%s' % 'Nenhuma palavra foi informada')
        else: 
            print('A maior palavra informada foi %s' % (maior))