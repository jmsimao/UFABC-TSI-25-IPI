from datetime import date

dia, mes, ano = input().split()

try:
    data = date(int(ano), int(mes), int(dia))
    output = 'DATA VALIDA'

except:
    output = 'DATA INVALIDA'

print(output)