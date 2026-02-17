laco = True

while (laco):
    try:
        literais = input().split()
        print('%s' % (str(literais[0])+str(literais[1])))

    except EOFError:
        laco = False
        break
