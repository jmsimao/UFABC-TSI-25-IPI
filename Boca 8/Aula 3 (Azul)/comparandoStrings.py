laco = True

while (laco):
    try:
        entrada = input().split()
        
        if (str(entrada[0]) == str(entrada[1])):
            print('iguais')
        else:
            print('diferentes')

    except EOFError:
        laco = False