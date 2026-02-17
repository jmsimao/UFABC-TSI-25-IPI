
def numerosPares100():
    pares = ''
    for i in range(1, 101):
        pares += (str(i) + ' ') if ((i % 2 )== 0) else ''

    return pares.rstrip()

literal = numerosPares100()
print('%s' % literal)
