qtde = int(input())

for i in range(0, qtde):
    pessoas = int(input())

    idioma = ''
    for p in range(0, pessoas):
        nativo = str(input())
        if (p == 0):
            idioma = nativo
        else:
            if (nativo != idioma):
                idioma = 'ingles'

    print('%s' % idioma)
