ano = int(input())

check = ano % 400

if (check == 0):
    print('ANO BISSEXTO')
else:
    if ((ano % 4 == 0) and (ano % 100 != 0)):
        print('ANO BISSEXTO')













