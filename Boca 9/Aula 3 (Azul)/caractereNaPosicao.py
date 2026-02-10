laco = True

while (laco):
    try: 
        dados = input().split()
        saida = str(dados[0])[int(dados[1])]
        print('%s' % (saida))

    except EOFError:
        laco = False