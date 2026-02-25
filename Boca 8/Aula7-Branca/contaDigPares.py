
laco = True
while laco:
    try:
        numero = input(); par = 0
        for i in range(len(numero)):
            if ((int(numero[i]) % 2) == 0):
                par += 1

        print('%d' % par)

    except:
        laco = False
