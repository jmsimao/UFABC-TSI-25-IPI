#from datetime import date
dia, mes, ano = input().split()
dia = int(dia); mes = int(mes); ano = int(ano)

def bissexto(pAno):
    return (pAno % 400 == 0) or ((pAno % 4 == 0) and (pAno % 100 != 0))

ultimosDias = [31,29 if bissexto(ano) else 28,31,30,31,30,31,31,30,31,30,31]

dia -= 1

if (dia == 0):
    mes -= 1

    if (mes == 0):
        mes = 12; ano -= 1
    
    dia = ultimosDias[mes-1]

dia = str(dia).zfill(2)
mes = str(mes).zfill(2)
ano = str(ano).zfill(4)

print(dia, mes, ano)