total = int(input())

for i in range(0, total):
    soma = 0
    qtde = int(input())

    for p in range(0, qtde):
        soma += int(input())

    print('%d' % (soma))