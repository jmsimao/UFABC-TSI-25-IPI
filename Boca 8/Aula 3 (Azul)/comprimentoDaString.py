laco = True

while (laco):
    try:
        entrada = input()
        
        print('%s' % len(str(entrada)))
        
    except EOFError:
        laco = False