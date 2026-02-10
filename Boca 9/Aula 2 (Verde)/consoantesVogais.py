tipoAlfabeto = ['vogal','consoante']
indice = 'aeiou'.find(str(input()).lower())
tipo = 0
if (not indice >= 0):
    tipo = 1
print('%s' % str(tipoAlfabeto[tipo]))