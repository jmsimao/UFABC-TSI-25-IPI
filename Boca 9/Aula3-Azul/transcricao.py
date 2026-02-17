laco = True

def transcrever(seqDNA):
    dna = 'CGTA'; rna = 'GCAU'
    seqRNA = ''

    for i in range(0, len(seqDNA)):
        p = dna.find(seqDNA[i])
        seqRNA += rna[p]

    return seqRNA

def saida(output):
    print('%s' % output)

while (laco):
    try:
        molecula = str(input());
        saida(transcrever(molecula))

    except:
        laco = False
        break
