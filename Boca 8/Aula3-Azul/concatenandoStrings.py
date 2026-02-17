laco = True

while (laco):
    try:
        entrada = input().split()
        
        print('%s%s' % (str(entrada[0]), str(entrada[1])))
      
    except EOFError:
        laco = False