infinito = True

while (infinito):
    soma = 0; continua = True 

    while (continua):
        try: 
            numero = input().split()

            if (len(numero) == 0):
                continua = False; infinito = continua
            else:
                for i in range(0, len(numero)):
                    soma += int(numero[i])
                print('%d' % (soma))
                soma = 0

        except:
            continua = False; infinito = continua