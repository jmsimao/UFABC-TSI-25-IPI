laco = True
vogais = 'aeiouAEIOU'

while (laco):
    try:
        r = 0; novaPalavra = ''
        literal = str(input())

        for i in range(len(literal)):
            if (vogais.find(literal[i]) == -1):
                novaPalavra += literal[i]
            else:
                r += 1

        print('%d %s' % (r, novaPalavra))

    except EOFError:
        laco = False
        break
