laco = True; anagrama = 'nao'

palavras = []; palavraInversa = []

def inverso(pal):
    ret = ""
    for i in range(len(pal)-1, -1, -1):
        ret = ret + pal[i]
    return ret

while (laco):

    try:
        pal = str(input())
        palavras.append(pal)
        palavraInversa.append(inverso(pal))

    except EOFError:
        laco = False

for i in range(0, len(palavras)):
    for c in range(0, len(palavras)):
        if (i != c and palavras[i] == palavraInversa[c]):
            anagrama = 'sim'

print('%s' % anagrama)