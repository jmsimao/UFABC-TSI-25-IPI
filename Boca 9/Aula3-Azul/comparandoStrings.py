laco = True

while (laco):
    try:
        literais = input().split()
        var1 = str(literais[0]); var2 = str(literais[1])

        if (var1 == var2):
            mensagem = "iguais"
        else:
            mensagem = "diferentes"

        print('%s' % mensagem)

    except EOFError:
        paco = False
        break
