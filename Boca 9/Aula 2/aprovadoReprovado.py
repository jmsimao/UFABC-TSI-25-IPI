valores = input()
nota = float(valores.split()[0])
faltas = int(valores.split()[1])

if (nota >= 6.0 and faltas <= 30):
    print('Aprovado!')
else:
    print('Reprovado!')