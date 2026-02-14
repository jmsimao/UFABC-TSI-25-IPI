palavra = str(input())
qtde = int(input())
laco = True
palavras = [''] * qtde


def anagrama(palavra, palavras):
    ret = 'nao'

    for i in range(0, len(palavras)):
        #print('%s' % palavras[i][::-1])
        if (palavra == palavras[i][::-1]):
            ret = 'sim'

    return ret

while (laco):
    try:

        for i in range(0, qtde):
            palavras[i] = str(input())

        print('%s' % anagrama(palavra, palavras))
        laco = False

    except EOFError:
        laco = False
        break
