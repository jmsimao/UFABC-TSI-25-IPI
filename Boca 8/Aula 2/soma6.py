soma = 0
numero = input().split()

for i in range(0, len(numero)):
    soma += int(numero[i])

print('%d' % (soma))