valores = input()
nota = float(valores.split()[0])
faltas = int(valores.split()[1])

if (nota >= 6.0 and faltas <= 30):
    print('Aprovado!')
elif (nota < 4.0 or faltas > 30):
    print('Reprovado!')
else:
    print('Exame Final!')