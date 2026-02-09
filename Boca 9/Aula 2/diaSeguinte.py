#from datetime import date
dia, mes, ano = input().split()

inicioGregoriano = ano + mes + dia
dia = int(dia); mes = int(mes); ano = int(ano)
ultimosDias = [31,28,31,30,31,30,31,31,30,31,30,31]
#print (len(ultimosDias))

if (mes != 2):
    if (dia <= 29):
        dia += 1
    elif (dia == 30):
        dia += 1
        if (ultimosDias[mes-1] != dia):
            dia = 1; mes += 1
            if (mes > 12):
                mes = 1; ano += 1
    elif (dia == 31):
        dia = 1; mes += 1
        if (mes > 12):
            mes = 1; ano += 1

else:
    #print('anoBissexto')
    anoBissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
   
    dia += 1
    if (dia == 29):
        if (not anoBissexto):
            dia = 1; mes = 3
    elif (dia == 30):
        dia = 1; mes = 3

## Fill
#dia = str(dia).zfill(2)
#mes = str(mes).zfill(2)
#ano = str(ano).zfill(2)

print('%s %s %s' % (str(dia).zfill(2), str(mes).zfill(2), str(ano).zfill(4)))