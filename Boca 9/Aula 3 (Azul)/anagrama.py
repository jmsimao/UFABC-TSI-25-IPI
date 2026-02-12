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


reading = True; count = 0

while (reading and count <= len(palavras)-1) :
  
    for i in range(0, len(palavraInversa)):
        if (count != i and palavras[count] == palavraInversa[i]):
            anagrama = 'sim'; reading = False

    count += 1

print('%s' % anagrama)