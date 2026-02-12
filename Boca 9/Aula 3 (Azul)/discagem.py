laco = True

alfabeto = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

while (laco):
    try:
        cel = str(input()).upper().replace('-','').replace(' ','').replace('.','')
        celNumerico = ''

        for i in range(0, len(cel)):
            if (cel[i] in '0123456789#*'):
                celNumerico += cel[i]
            else:
                numero = 0
                for c in alfabeto:
                    if (c.find(cel[i]) >= 0):
                        celNumerico += str(numero + 2)
                    numero += 1

        print('%s' % celNumerico)

    except EOFError:
        laco = False
        break


