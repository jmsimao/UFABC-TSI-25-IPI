#from datetime import date

dia, mes, ano = input().split()

inicioGregoriano = ano + mes + dia
dia = int(dia); mes = int(mes); ano = int(ano)
mensagem = "DATA INVALIDA"
invalida = False
ultimosDias = [31,28,31,30,31,30,31,31,30,31,30,31]
anoBissexto = False
#print (len(ultimosDias))

if ((dia < 1 or dia > 31) or (mes < 1 or mes > 12) or (ano < 1582)):
    #print('Dia: %d, mês: %d ou ano: %d inválido(s)!' % (dia, mes, ano))
    invalida = True

# Calendario Gregoriano
if (not invalida and int(inicioGregoriano) < int(15821015)):
    #print('Inicio do Calendario Gregoriano!')
    invalida = True

# Verifica ultimo dia do mês
if (not invalida and (mes != 2)):
    #print('mes verificando %d' % mes)
    if (dia > ultimosDias[mes-1]):
          #print('Dia: %d, mês: %d' % (dia, mes))
          invalida = True

# Ano Bissexto = 29/02
if (not invalida and dia == 29 and mes == 2):
    if (ano % 4 != 0):
        #print('passo 1')
        invalida = True 
        
    if ((not invalida) and (ano % 100 == 0) and (ano % 400 != 0)):
        #print('passo 2, ano por 100: %.2f, ano por 400: %.2f' % (float(ano % 100), float(ano % 400)))
        invalida = True

    #if (invalida):
    #    print('Erro ano bissexto: dia %d, mês %d.' % (dia, mes))

# Data válida
if not invalida:
    mensagem = "DATA VALIDA"

print('%s' % mensagem)